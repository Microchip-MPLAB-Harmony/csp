export declare class PluginService {
    private readonly pluginConfig;
    private readonly _initArgs;
    private readonly _portAddress;
    constructor();
    private readJSONAsync;
    absolutePath(relativePath: string): string;
    frameworkRoot(): string;
    openURL(relativePath: string): void;
    private readJSON;
    get initArgs(): Map<string, object>;
    get portAddress(): number;
}
export declare const pluginService: PluginService;
