//-------------------------------------------------------------------------------
// Circle pattern
// Vishang Shah
//
// Inpired from mmalex
// https://www.shadertoy.com/user/mmalex
//
//-------------------------------------------------------------------------------
vec4 newPattern(void)
{
	vec4 pixelColor = vec4(0.5,0.5,0.5,1.0);

	vec2 uv = gl_FragCoord.xy*(1.0/128.0);
	float res = min(iResolution.x, iResolution.y);
	float pixel = 1.0/res;
	vec2 p = (gl_FragCoord.xy - iResolution.xy * 0.5) * pixel;
	float h = texture2D(iChannel0, uv).x;
	float h2 = texture2D(iChannel0, uv + vec2(0.001,0.002)).x;

	float ink = 0.0, theta = 0.0;

	float t = (0.00005*iGlobalTime);
    
	for(int i = 0; i < 20; i++)
	{
		ink += max(0.0, 1.2 - abs(length(p) - 0.5) * res);
		res = res/1.15;
		p *= -1.15;
		p.x += sin(theta) * t * float(i);
		p.y += cos(theta) * t * float(i);
		theta += iGlobalTime * 0.1;

	}
    p = (gl_FragCoord.xy - iResolution.xy * 0.5) * pixel;
    res = min(iResolution.x, iResolution.y);
    theta = 0.0;
    for(int j = 0; j < 10; j++)
	{
		ink += max(0.0, 1.1 - abs(length(p) - 0.8) * res);
		res = res/1.15;
		p *= 1.15;
		p.x -= sin(theta) * t * float(j);
		p.y -= cos(theta) * t * float(j);
		theta -= iGlobalTime * 0.2;

	}
	
	//ink = 1.0 - ink;
    
	pixelColor = vec4(ink, ink , ink,1.0);
	return pixelColor;
}
//-------------------------------------------------------------------------------
void main(void)
{	
	
	gl_FragColor=newPattern();

}

