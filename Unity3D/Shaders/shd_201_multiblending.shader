﻿
// Shader 		: 	Multi Blending
// Author 		: 	Vishang Shah (vishangshah.com)
// Description 	: 	This shader blends between two texture sets based on texture and vertex alpha channels.
//					
//
// Defining category and name of the shader
Shader "MyShaders/Pixel Techniques/201 MultiBlending"
{
	// Here we define properties exposed in the material for user to control
	Properties
	{
		// Ambient color as float4
		_AmbientColor ("Ambient Color", Color) = (1.0, 1.0, 1.0, 1.0)	
		// Defining Diffuse color property as a float4
		_DiffuseColor ("Diffuse Color", Color) = (1.0, 1.0, 1.0, 1.0)
		// Defining Specular color as float4
		_SpecularColor ("Specular Color", Color) = (1.0, 1.0, 1.0, 1.0)
		// Defininig Specular Shininess as float range
		_Shininess ("Shininess", Range(1.0, 10.0)) = 1.0
		// Rim Color as float4
		_RimColor ("Rim Color", Color) = (1.0, 1.0, 1.0, 1.0)
		// Rim Intensity as float range
		_RimIntensity ("RimIntensity", Range(0.5, 2.0)) = 1.0
		// Texture Map
		_MainTex("Diffuse Texture", 2D) = "white" {}
	}
	// There can be multiple shaders based on platform? GPU? Deployment?
	SubShader
	{
		// There can be multiple passes of calculation
		Pass
		{
			// Tags to tell shader the lighting model
			// It's important to include this otherwise the dynamic lights will not be considered
			//
			Tags { "LightMode" = "ForwardBase" }
			// This is where CG shader code starts in Unity3D shader
			CGPROGRAM
			
			// Providing names of vertex and fragment functions for each shader
			#pragma vertex 		vertexCode
			#pragma fragment 	fragmentCode

			// User defined variables (mostly from Propeties above)
			uniform float4 _AmbientColor;
			uniform float4 _DiffuseColor;
			uniform float4 _SpecularColor;
			uniform float  _Shininess;
			uniform float4 _RimColor;
			uniform float  _RimIntensity;

			uniform sampler2D _MainTex;
			uniform float4 _MainTex_ST;

			// Unity Defined Variables
			// Color of the light
			uniform float4 _LightColor0;

			// Variables to move data to and from both shaders

			// Structs
			// As we are going to deal with more properties of vertices than just position,
			// It's better to use structures (a la C/C++), to package per-vertex properties
			//
			// Structure to pass data from application to vertex shader
			struct vertexIn
			{
				// vertex position with semantic POSITION
				//
				float4 vertPos 	: POSITION;
				// vertex normals - semantic normal
				float3 vertNorm	: NORMAL;
				// UV coordinates
				float4 texcoord : TEXCOORD0;
			};
			//
			// Structure to pass data from vertex shader to fragment shader
			struct fragmentIn
			{
				// fragment position as a result of transformation in vertex shader
				float4 fragPos 	: SV_POSITION;
				// As you can see we are using UV coordinates 2 to pass transformed normals to FS
				float3 fragNorm	: TEXCOORD2;
				float4 posWorld : TEXCOORD3;
				float4 fragCol  : COLOR;
				// UV coordinates
				float4 tex 		: TEXCOORD0;
			};
			//
	
			// Vertex Shader

			//
			fragmentIn vertexCode(vertexIn vertIn)
			{
				fragmentIn fragIn;
				// To get fragment position,
				// Multiplying vertex position with ModelViewProjection matrix in Unity3D
				fragIn.fragPos 	= mul(UNITY_MATRIX_MVP, vertIn.vertPos);

				// Calculating Normal Direction
				fragIn.fragNorm = normalize(mul(float4(vertIn.vertNorm,0.0), _World2Object).xyz);

				// Calculating pixel world position (to derive view direction)
				fragIn.posWorld = mul(_Object2World, vertIn.vertPos);

				// Passing UV coordinates
				fragIn.tex = vertIn.texcoord;

				return fragIn;

			}

			// Fragment Shader
			// In this shader, we are going to calculate lighting in fragment shader
			// It will be expensive to run on GPUs, compared to vertex lit lighting
			// But it will be of higher quality
			//
			float4 fragmentCode(fragmentIn fragIn) : COLOR
			{

				// Calculating Light Direction
				float3 lightDirection = normalize(_WorldSpaceLightPos0).xyz;
				// Diffuse Term
				// This is basically N.L contribution + Texture

				

				float3 diffuseTerm = _LightColor0 * _DiffuseColor * max(dot(fragIn.fragNorm, lightDirection),0.0);

				// Specular Term
				// Phong Specular is calculated from Ks * (R.V)^shininess
				// Here R is Reflection vector of Light calculated from shader intrinsic reflect()
				//
				float3 viewDirection = normalize(_WorldSpaceCameraPos - fragIn.posWorld).xyz;
				float3 lightReflectDir = reflect(-lightDirection, fragIn.fragNorm);
				float3 specularTerm = _SpecularColor * pow(max(dot(lightReflectDir, viewDirection),0.0),_Shininess) * max(dot(fragIn.fragNorm, lightDirection),0.0);
				
				// Rim Term
				float4 rim = 1 - saturate(dot(fragIn.fragNorm, viewDirection));

				float3 rimTerm = rim * max(dot(fragIn.fragNorm, lightDirection),0.0);
				rimTerm = pow(_RimColor * rimTerm,_RimIntensity);

				// Texture Map
				float4 tex = tex2D(_MainTex, _MainTex_ST.xy * fragIn.tex.xy + _MainTex_ST.zw);

				// Final color contribution by adding all terms
				fragIn.fragCol = tex * float4(_AmbientColor.xyz + diffuseTerm + specularTerm + rimTerm, 1.0);

				// Returning calculated fragment color
				return fragIn.fragCol;
			}

			// End of CG code
			ENDCG
		}
	}
}
