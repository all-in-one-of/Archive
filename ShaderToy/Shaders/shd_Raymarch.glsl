// shd_Raymarch
// Vishang Shah

float map( in vec3 p)
{
    vec3 q = mod(p * 1.0, 4.0) - 2.0;
 	float d1 = length(q) - 1.0;
    d1 += 0.1* sin(iGlobalTime + p.x * 10.0) * sin(iGlobalTime + p.y * 10.0) * sin(iGlobalTime + p.z * 10.0);
    
    float d2 = p.y + 1.0;
    
    return min(d1, d2);

}

vec3 calcNormal(in vec3 p)
{
    vec2 e = vec2(0.0001, 0.0);
    vec3 nor;
	nor.x = map(p+e.xyy) - map(p-e.xyy);
    nor.y = map(p+e.yxy) - map(p-e.yxy);
    nor.z = map(p+e.yyx) - map(p-e.yyx);
    return normalize(nor);
}

void main(void)
{
	vec2 uv = gl_FragCoord.xy / iResolution.xy;
    vec2 p = -1.0 + 2.0 * uv;
    p.x *= iResolution.x/iResolution.y;
    
    vec3 ro = vec3(0.0,0.0,2.0);
    vec3 rd = normalize(vec3(p, -1.0));
    
    vec3 col = vec3(0.0);
    
    float tmax = 20.0;
    float h = 1.0;
    float t = 0.0;
    for(int i=0; i < 100; i++)
    {
        if( h < 0.001 || t > tmax) break;
   		h = map(ro + t * rd);   
        t+= h;
    }
    
    vec3 light = vec3(0.55);
    
    if(t < tmax)
    {
        vec3 pos = ro + t*rd;
        vec3 nor = calcNormal(pos);
        col = vec3(1.0);
        col *= nor.z;
        col = vec3(0.0,0.2,0.8) * clamp(dot(nor,light), 0.0, 1.0);
        col += vec3(0.2,0.3,0.5) * clamp(nor.y, 0.0,1.0);
        col += 0.1;
        
        col *= exp(-t * 0.07);
        
        
    }
    
	gl_FragColor = vec4(col,1.0);
}
