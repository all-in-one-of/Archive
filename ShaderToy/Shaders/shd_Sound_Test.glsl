// shd_Sound_Test
// Vishang Shah

void main(void)
{
	vec2 uv = gl_FragCoord.xy / iResolution.xy;
    
	vec2 p = uv - 0.5;
    float r = length(p);
    float a = atan(p.x, p.y);
    
    vec4 sound = texture2D(iChannel1, vec2(0.01, 0.01));
    vec4 tex = texture2D(iChannel0, vec2(10.0 / r * 0.1 * sound.x, a));
    
    vec3 c = tex.xyz * r;
    
	gl_FragColor = vec4(c,1.0);
}