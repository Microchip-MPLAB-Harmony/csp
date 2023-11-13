/// <reference types="react" />
export declare let globalSymbolStyleData: Map<any, Map<string, string>>;
export declare let globalSymbolSStateData: Map<any, any>;
export declare let defaultInputNumberStyleMap: Map<string, string>;
export declare let defaultDropDownStyleMap: Map<string, string>;
export declare enum SymbolType {
    DropDown = 0,
    InputNumber = 1,
    CheckBox = 2,
    String = 3
}
export declare function GetMinFractionValueBasedSymbolType(componentId: any, symbolID: any): 1 | 0;
export declare function GetUIComponentWithLabel(props: {
    componentId: any;
    symbolId: any;
    symbolListeners: any;
    onChange: (arg0: any) => void;
}): JSX.Element;
export declare function GetUIComponentWithOutLabel(props: {
    componentId: any;
    symbolId: any;
    symbolListeners: any;
    onChange: (arg0: any) => void;
}): JSX.Element;
export declare function GetStyle(symbolId: string): {
    [k: string]: string;
} | undefined;
export declare function StoreSymbolStyle(toolBarHeight: string, symbolId: string, styleMap: Map<any, any>): void;
export default class Components {
}
