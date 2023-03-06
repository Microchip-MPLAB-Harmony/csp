export declare class SVGSymbolStyleService {
    private readonly a;
    private readonly symbolsArray;
    private readonly labelsArray;
    constructor(symbolStylesJSON: any, dynamicSymbolsIgnoreList: string[]);
    ReadJSONData(symbolStylesJSON: any, dynamicSymbolsIgnoreList: string[]): void;
    flushStore(): void;
    get abcd(): number;
}
