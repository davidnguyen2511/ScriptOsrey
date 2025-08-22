const fs = require("fs");
const path = require("path");

const sourceDir = "D:\\web\\data";
const targetDir = "D:\\WebServer\\image_copy\\data"; 

let filesList = fs.readdirSync(sourceDir).filter(file => fs.statSync(path.join(sourceDir, file)).isFile());


function copyRandomImage() {
    if (filesList.length === 0) {
        console.log("not have emage.");
        const imageExtensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'];

        try {
            filesList = fs.readdirSync(sourceDir).filter(file => fs.statSync(path.join(sourceDir, file)).isFile());

        } catch (err) {
            console.error('error:', err);
        }
        
    }
    
    const randomIndex = Math.floor(Math.random() * filesList.length); 
    const fileName = filesList.splice(randomIndex, 1)[0]; 
    const sourcePath = path.join(sourceDir, fileName);
    const timestamp = Date.now();
    const newFileName = `${timestamp}_${fileName}`;
    const targetPath = path.join(targetDir, newFileName);

    fs.readFile(sourcePath, (err, data) => {
        if (err) {
            console.error(`error ${fileName}:`, err);
            return;
        }

        fs.writeFileSync(targetPath, data);
	console.log("time", new Date().toLocaleString());
    });
}

setInterval(copyRandomImage, 1000);
