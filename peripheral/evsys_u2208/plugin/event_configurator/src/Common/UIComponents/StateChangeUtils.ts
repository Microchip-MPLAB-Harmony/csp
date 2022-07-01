import { globalSymbolSStateData } from "./UIComponentCommonUtils";

export function ChangeClassNameState(symbolId: string, className: any) {
  globalSymbolSStateData.get(symbolId).changeClassNameState(className);
}

export function ChangeValueState(symbolId: string, symbolValue: any) {
  globalSymbolSStateData.get(symbolId).changeValue(symbolValue);
}

export function ChangeReadOnlyState(symbolId: string, readOnlyStatus: any) {
  globalSymbolSStateData
    .get(symbolId)
    .changeReadOnlyStatus(readOnlyStatus);
}

export function ChangeStyleState(symbolId: string, styleObject: any) {
  globalSymbolSStateData.get(symbolId).changeStyleState(styleObject);
}

export function ChangeVisibleState(symbolId: string, visibleStatus: any) {
  globalSymbolSStateData
    .get(symbolId)
    .changeVisibleStatus(visibleStatus);
}

export function ChangeComponentState(
  symbolId: string,
  symbolValue: any,
  readOnlyStatus: any,
  visibleStatus: any
) {
  globalSymbolSStateData
    .get(symbolId)
    .changeComponentState(
      symbolValue,
      readOnlyStatus,
      visibleStatus
    );
}
