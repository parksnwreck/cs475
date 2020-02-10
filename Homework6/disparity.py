import numpy as np
def disparity(leftimg, rightimg, halfpatchsize, maxdisp=None):
	"""DISPARITY Calculates the disparity for a pair of rectified stereo images.
	  DISPMATRIX = DISPARITY(LEFTIMG, RIGHTIMG, HALFPATCHSIZE, MAXDISP) calculates
	  the pointwise disparity between a pair of rectified stereo images.

	  LEFTIMG is the left image of the stereo pair, while RIGHTIMG is the
	  right image.

	  HALFPATCHSIZE specifies half of the patch size (M in the problem
	  statement in the homework). The patch size actually used ends up being
	  2*HALFPATCHSIZE + 1.

	  MAXDISP is an optional parameter specifying the maximum absolute
	  disparity to be tested for. If omitted, it defaults to HALFPATCHSIZE.

	  The output argument DISP should contain the disparity between the two
	  images at every point where a valid patch comparison can be made. Note
	  that, due to boundary effects, the size of DISPMATRIX will be smaller.
	"""

	if maxdisp is None:
	 	maxdisp = halfpatchsize


	#get image dimensions
	nrows, ncols = leftimg.shape

	if nrows != rightimg.shape[0] or ncols != rightimg.shape[1]:
	 	raise ValueError("Left and right images aren't of the same size")


	#make sure you understand why the disparity matrix will be smaller than the input images!
	dispmatrix = np.zeros((np.array(leftimg.shape) - 2*halfpatchsize - np.array([0, 2*maxdisp])))

	#range of values for the central patch positions
	y0s = np.arange(halfpatchsize:(nrows - halfpatchsize))
	x0s = np.arange((halfpatchsize + maxdisp):(ncols - halfpatchsize - maxdisp))

	for j in range(len(x0s))
	    for i in range(len(y0s))

	        #get actual (x0,y0) position in the image
	        x0 = x0s[j] #this is the horizontal index (col)
	        y0 = y0s[i] #this is the vertical index (row)


			# YOUR CODE HERE


	        dispmatrix[i,j] = #disparity value found for current position;


