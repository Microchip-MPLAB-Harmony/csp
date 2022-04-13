import { component_id } from "../UI/MainView/MainBlock";
export function GetSymbolValue(componentId: any, value: any) {
  try {
    let symValue = (window as any).javaConnector.getSymbolData(
      componentId,
      value
    );
    return symValue;
  } catch (err) {
    ErrorMessage(err);
  }
}

function ErrorMessage(err: any) {
  alert(
    "Please update latest harmony-services pacakge. Unable to access symbol editable status:  " +
      err
  );
}

export function GetSymbolArray(componentId: any, value: any) {
  try {
    let symbolArray = (window as any).javaConnector.getSymbolValues(
      componentId,
      value
    );
    if (symbolArray === null) {
      let temp: never[] = [];
      return temp;
    }
    let array = symbolArray.split("M*C");
    return array;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolLabelName(componentId: any, value: any) {
  try {
    let labelName = (window as any).javaConnector.getSymbolLabelName(
      componentId,
      value
    );
    return labelName;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolMinValue(componentId: any, value: any) {
  try {
    let minValue = (window as any).javaConnector.getSymbolMinValue(
      componentId,
      value
    );
    return minValue;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolMaxValue(componentId: any, value: any) {
  try {
    let maxValue = (window as any).javaConnector.getSymbolMaxValue(
      componentId,
      value
    );
    return maxValue;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolType(componentId: any, value: any) {
  try {
    let symbolType = (window as any).javaConnector.getSymbolType(
      componentId,
      value
    );
    return symbolType;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolVisibleStatus(componentId: any, value: any) {
  try {
    let symbolVisibleStatus = (
      window as any
    ).javaConnector.getSymbolVisibleStatus(componentId, value);
    return symbolVisibleStatus;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function GetSymbolEnableStatus(componentId: any, value: any) {
  try {
    let symbolEnableStatus = (
      window as any
    ).javaConnector.getSymbolEnableStatus(componentId, value);
    return symbolEnableStatus;
  } catch (err) {
    ErrorMessage(err);
  }
}

export function UpdateSymbolValue(
  componentId: any,
  symbolId: any,
  symbolValue: any
): void {
  try {
    (window as any).javaConnector.updateSymbolData(
      componentId,
      symbolId,
      symbolValue
    );
  } catch (err) {
    ErrorMessage(err);
  }
}

export function SetComponentId(component_id: any): void {
  try {
    (window as any).javaConnector.setComponentId(component_id);
  } catch (err) {
    ErrorMessage(err);
  }
}

export function AddSymbolListner(symbolId: any): void {
  try {
    (window as any).javaConnector.addSymbolListener(symbolId);
  } catch (err) {
    ErrorMessage(err);
  }
}

export function clearSymbol(componentId: any, symbolId: any): void {
  try {
    (window as any).javaConnector.clearSymbol(componentId, symbolId);
  } catch (err) {
    ErrorMessage(err);
  }
}

export function ZoomInReact() {
  try {
    (window as any).javaConnector.ZoomInReactCall();
  } catch (err) {
    ErrorMessage(err);
  }
}

export function ZoomOutReact() {
  try {
    (window as any).javaConnector.ZoomOutReactCall();
  } catch (err) {
    ErrorMessage(err);
  }
}
