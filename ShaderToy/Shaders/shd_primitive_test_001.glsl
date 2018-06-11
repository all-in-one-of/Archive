
// Inspired from
// https://www.shadertoy.com/view/4sXGD2

#define MAX_MARCHING_STEPS 68

const float PIXEL_EPS 		= 1.0;
const float DICONT_FACTOR	= 3.0;
const float FAR 			= 20.0;
const float FOCAL_LENGTH 	= 4.0;

const float TEXTURE_SIZE	= 512.0;
const float BUMP_INTENSITY	= 5.0;

// Constants
const float SQRT8			= 2.8284271247461903;
const float PI              =  3.141592653589793;

// Trig Functions

float rotations(float x)	{ return x * (0.5/PI); }
vec2  cossin(float a)		{ return vec2(cos(a), sin(a)); }
float atan_yx(vec2 p)		{ return atan(p.y, p.x); }



void main(void)
{
	vec2 uv = gl_FragCoord.xy / iResolution.xy;
	gl_FragColor = vec4(uv,0.5+0.5*sin(iGlobalTime),1.0);
}

