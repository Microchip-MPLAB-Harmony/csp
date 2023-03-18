export declare function GetColeredStyledObject(labelId: string, changeColorStatus: boolean, changeColor: string): {
    [k: string]: any;
} | undefined;
export declare function GetBoldStyledObject(labelId: any, boldStatus: boolean): {
    [k: string]: any;
} | undefined;
export declare function AddPlainLabel(labelId: string, text: any): JSX.Element | undefined;
export declare function AddPlainLabelWithBold(labelId: string, text: any, boldStatus: boolean): JSX.Element | undefined;
export declare function AddSymboLabelWithSuffix(labelId: string, component_id: any, symbolId: any, suffix: string): JSX.Element | undefined;
export declare function AddSymboLabelWithSuffixWithBold(labelId: string, component_id: any, symbolId: any, suffix: string, boldStatus: boolean): JSX.Element | undefined;
export declare function AddMinMaxSymboLabelWithSuffix(labelId: string, component_id: string, symbolId: any, suffix: string, minValue: any, maxValue: any, changeColor: any, labelTooltip: any): JSX.Element | undefined;
export declare function AddPrefixDivSymbolLabel(id: string, component_id: string, symbolId: string, InputFormat: (arg0: any) => void): JSX.Element | undefined;
