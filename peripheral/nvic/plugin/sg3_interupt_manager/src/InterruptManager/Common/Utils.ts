import { component_id } from "../UI/MainView/MainBlock";
import {
  clearSymbol,
  GetSymbolArray,
  GetSymbolValue,
  UpdateSymbolValue,
} from "./SymbolAccess";

export function getIndex(selectedValue: any, array: any) {
  return array.findIndex((obj: any) => obj === selectedValue);
}

export function convertToBoolean(input: string): boolean {
  try {
    return JSON.parse(input);
  } catch (e) {
    return false;
  }
}

export function clearAllSymbols(mc_component_id: any, symbolsArray: string[]) {
  return symbolsArray.map((object: any) =>
    clearSymbol(mc_component_id, object)
  );
}

export function StroeSymbolArrayToMap(
  map: Map<String, Object>,
  componentId: any,
  symbolArray: String[]
) {
  for (let index in symbolArray) {
    map.set(
      symbolArray[index],
      GetSymbolValue(componentId, symbolArray[index])
    );
  }
  return map;
}

export function UpdateArrayofSymbolsResetAction(
  map: Map<String, Object>,
  componentId: any,
  symbolArray: String[]
) {
  for (let index in symbolArray) {
    UpdateSymbolValue(
      componentId,
      symbolArray[index],
      map.get(symbolArray[index])
    );
  }
}

export function AddDynamicSymbols(
  symbol: string,
  apend: string,
  symbolArry: string[]
) {
  let symbolArray = GetSymbolArray(component_id, symbol);
  for (let index in symbolArray) {
    let newSymbol = symbol + "_" + apend + "_" + symbolArray[index];
    if (!symbolArray.includes(newSymbol)) {
      symbolArry.push(newSymbol);
    }
  }
  return symbolArry;
}


