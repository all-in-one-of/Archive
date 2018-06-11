
window.onerror = function(msg, url, lineno)
{
	alert(url + '(' + lineno + '):' + msg);
}

function screenQuad()
{
	// Screen Quad
	var vertexPosBuffer = gl.createBuffer();
	gl.bindBuffer(gl.ARRAY_BUFFER, vertexPosBuffer);

	/*
	2___3
	|\	|
	| \	|
	|__\|
	0	1
	*/
	var maxExtent = 0.7;
	var minExtent = -maxExtent;

	var vertices = [minExtent, minExtent, maxExtent, minExtent, minExtent, maxExtent, maxExtent, maxExtent];
	gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
	vertexPosBuffer.itemSize = 2;
	vertexPosBuffer.numItems = 4;

	return vertexPosBuffer;

}