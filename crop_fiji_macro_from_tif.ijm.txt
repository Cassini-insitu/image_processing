


inputDir = "";
outputDir =""

print("Input directory: " + inputDir);
print("Input directory2: " + inputDir);
list = getFileList(inputDir);



// Print the list of input files
for (i = 0; i < list.length; i++) {
    print("Input file: " + list[i]);
}

for (i = 0; i < list.length; i++) {
	print("Processing: ");
    inputFilePath = inputDir + "/" + list[i];
    print("Processing2: " + list[i]);
    filename = list[i];
    print("Processing: " + filename);
    filenameWithoutExtension = filename;
    print("Processing4: " + inputFilePath);
    open(inputFilePath);

    print("Processing5: " + filename);
    x = 0;    // Starting x-coordinate of the crop
    y = 0;    // Starting y-coordinate of the crop
    width = 7616;  // Width of the cropped region
    height = 4816; // Height of the cropped region

	makeRectangle(x, y, width, height);
    run("Crop");

	makeRectangle(x, y, width, height);
    run("Crop");

	Image_out = outputDir + filename;
	print("Processing8: " + Image_out);

	saveAs("Tiff", Image_out);
	close("*");
}	