class FileNode {
  children = new Map<string, FileNode>();
  content = "";
  isFile = false;
}

class FileSystem {
    root: FileNode;
    private split(path: string) {
        return path.split("/").filter(Boolean);
    }
    private walk(path: string) {
        let node = this.root;
        for (const segment of this.split(path)) {
            if (!node.children.has(segment)) {
                node.children.set(segment, new FileNode());
            }
            node = node.children.get(segment);
        }
        return node;
    }
    constructor() {
        this.root = new FileNode();
    }
    /**
     * @param {string} path
     * @return {string[]}
     */
    ls(path: string): string[] {
        const node = this.walk(path);
        if (node.isFile) {
            const segments = this.split(path);
            return [segments[segments.length - 1]];
        }
        return [...node.children.keys()].sort();
    }

    /**
     * @param {string} path
     * @return {void}
     */
    mkdir(path: string): void {
        this.walk(path);
    }

    /**
     * @param {string} filePath
     * @param {string} content
     * @return {void}
     */
    addContentToFile(filePath: string, content: string): void {
        const node = this.walk(filePath);
        node.isFile = true;
        node.content += content;
    }

    /**
     * @param {string} filePath
     * @return {string}
     */
    readContentFromFile(filePath: string): string {
        return this.walk(filePath).content;
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * let obj = new FileSystem();
 * let param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath, content);
 * let param_4 = obj.readContentFromFile(filePath);
 */
