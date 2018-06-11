// ------------------------------------------------------------------------------
// shd_Checker
// Procedural Checker pattern
// Vishang Shah
// ------------------------------------------------------------------------------

#define tiles 20.0

void main(void)
{
	vec2 uv = gl_FragCoord.xy / iResolution.xy;
    float aspect = iResolution.x/iResolution.y;
    
	float xy = 0.0;
    
    vec4 white = vec4(1.0,1.0,1.0,1.0);
    vec4 black = vec4(0.0,0.0,0.0,1.0);
    vec4 color = vec4(0.0,0.0,0.0,1.0);
    
    float TileCount = tiles * (1.0 + 0.5 * sin(iGlobalTime - tiles/2.0));
    
    if(mod(uv.x * TileCount * aspect,2.0) > 1.0)
    {
        if(mod(uv.y * TileCount,2.0) > 1.0)
        	color = white;
       	else
            color = black;
    }
    else
    {
        if(mod(uv.y * TileCount,2.0) < 1.0)
        	color = white;
        else
            color = black;
    }
    
	//gl_FragColor = vec4(uv,0.5+0.5*sin(iGlobalTime),1.0);
    gl_FragColor = vec4(color.xy, (0.5 + 0.5 * sin(iGlobalTime)),1.0);
}
