export declare class PluginService {
    private readonly pluginConfig;
    private readonly _initArgs;
    constructor();
    private readJSONAsync;
    absolutePath(relativePath: string): string;
    frameworkRoot(): string;
    openURL(relativePath: string): void;
    private readJSON;
    get initArgs(): Map<string, object>;
}
export declare const pluginService: PluginService;
