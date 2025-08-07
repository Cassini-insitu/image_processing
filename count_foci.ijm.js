inputDir = "/Volumes/External_1/scope_images/HCR/HCR/crop/";
outputDir = "/Volumes/External_1/scope_images/HCR/HCR/foci_80_90_120/";


print("Input directory: " + inputDir);
print("Input directory2: " + inputDir);
list = getFileList(inputDir);


function processChannel(channel, prominence, minDisplay, maxDisplay) {
	run("Remove Overlay");
	run("Select None");
	run("Clear Results");
	titi="C" + channel + "-" + tit;
	selectWindow(titi);
	run("Set Scale...", "distance=1 known=1 pixel=1 unit=um");


	run("Find Maxima...", "prominence=" + prominence + " output=[Point Selection]");
	
	run("Measure");
	savePathCoord = outputDir + "C" + channel + "-" + name_file + ".csv";
	saveAs("Results", savePathCoord);
	setMinAndMax(minDisplay, maxDisplay);
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	run("In [+]", "slice");
	wait(5000);

	run("Flatten");

	savePathTiffOverlay = outputDir + "C" + channel + "-" + name_file + "overlay.tif";    
	//Save the current channel image with points
	saveAs("Tiff", savePathTiffOverlay);
	wait(5000);
}

for (i = 0; i < list.length; i++) {
	if (endsWith(list[i].toLowerCase(), ".tif")) {
		print("Processing: ");
	    inputFilePath = inputDir + "/" + list[i];
	    name_file = replace(list[i], ".tif", "");
	    open(inputFilePath);
		tit= getTitle();
		run("Split Channels");
	
		processChannel(1, 80, 100, 1000);  
		processChannel(2, 90, 100, 1000);
		processChannel(4, 120, 100, 700);
		run("Close All");
	}
}