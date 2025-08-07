// Set input and output directories
inputDir = "";
outputDir = inputDir + "converted_tiffs/";
File.makeDirectory(outputDir);

// Get list of files in input directory
fileList = getFileList(inputDir);

for (i = 0; i < fileList.length; i++) {
    if (endsWith(fileList[i], ".ims")) {
        fullPath = inputDir + fileList[i];
        print("Opening: " + fullPath);

        // Use Bio-Formats to open the IMS file
        run("Bio-Formats Importer", "open=[" + fullPath + "] autoscale color_mode=Composite view=Hyperstack stack_order=XYCZT");

        // Remove extension from filename
        name = substring(fileList[i], 0, lastIndexOf(fileList[i], "."));

        // Save as multi-channel TIFF
        saveAs("Tiff", outputDir + name + ".tif");

        // Close all images forcefully
        closeAllWindowsAndImages();

        // Run Java garbage collector
        run("Collect Garbage");
    }
}

function closeAllWindowsAndImages() {
    n = nImages;
    while (n > 0) {
        selectImage(n);
        close();
        n = n - 1;
    }
    // Extra cleanup
    run("Close All");
    wait(1000); // slight delay to allow full cleanup
}
