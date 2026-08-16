class FileNode {
    children: Map<string, FileNode>;
    isFile: boolean;
    content: string;
    constructor() {
        this.children = new Map();
        this.isFile = false;
        this.content = "";
    }
}

class FileSystem {
    root: FileNode;
    private splitPath(path: string): string[] {
        return path.split('/').filter(Boolean);
    }
    private walk(path: string) {
        let node = this.root;
        for (const segment of this.splitPath(path)) {
            if (!node.children.has(segment)) node.children.set(segment, new FileNode());
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
        const segment = this.walk(path);
        if (segment.isFile) {
            const parts = this.splitPath(path);
            return [parts[parts.length - 1]];
        }
        return [...segment.children.keys()].sort();
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
        const file = this.walk(filePath);
        file.isFile = true;
        file.content += content;
    }

    /**
     * @param {string} filePath
     * @return {string}
     */
    readContentFromFile(filePath: string): string {
        const file = this.walk(filePath);
        return file.content;
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
