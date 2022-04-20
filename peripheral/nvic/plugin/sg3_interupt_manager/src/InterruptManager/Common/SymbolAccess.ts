import { component_id } from "../UI/MainView/MainBlock";
export function GetSymbolValue(componentId: any, value: any) {
  try {
    let symValue = (window as any).javaConnector.getSymbolData(
      componentId,
      value
    );
    return symValue;
  } catch (err) {
    ErrorMessage("GetSymbolValue", value, err);
  }
}

function ErrorMessage(message : any, symbolId : any,err: any) {
  alert(
    "Please update latest harmony-services pacakge. Unable to access generic plugin API :  "+ message +  " and symbol Id : "+ symbolId+" ->"+
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
    ErrorMessage("GetSymbolArray",value, err);
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
    ErrorMessage("GetSymbolLabelName", value,err);
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
    ErrorMessage("GetSymbolMinValue", value,  err);
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
    ErrorMessage("GetSymbolMaxValue", value, err);
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
    ErrorMessage("GetSymbolType", value, err);
  }
}

export function GetSymbolVisibleStatus(componentId: any, value: any) {
  try {
    let symbolVisibleStatus = (
      window as any
    ).javaConnector.getSymbolVisibleStatus(componentId, value);
    return symbolVisibleStatus;
  } catch (err) {
    ErrorMessage("GetSymbolVisibleStatus", value, err);
  }
}

export function GetSymbolEnableStatus(componentId: any, value: any) {
  try {
    let symbolEnableStatus = (
      window as any
    ).javaConnector.getSymbolEnableStatus(componentId, value);
    return symbolEnableStatus;
  } catch (err) {
    ErrorMessage("GetSymbolEnableStatus", value, err);
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
    ErrorMessage("UpdateSymbolValue", symbolId, err);
  }
}

export function SetComponentId(component_id: any): void {
  try {
    (window as any).javaConnector.setComponentId(component_id);
  } catch (err) {
    ErrorMessage(SetComponentId, component_id, err);
  }
}

export function AddSymbolListner(symbolId: any): void {
  try {
    (window as any).javaConnector.addSymbolListener(symbolId);
  } catch (err) {
    ErrorMessage("AddSymbolListner", symbolId, err);
  }
}

export function clearSymbol(componentId: any, symbolId: any): void {
  try {
    (window as any).javaConnector.clearSymbol(componentId, symbolId);
  } catch (err) {
    ErrorMessage("clearSymbol",symbolId, err);
  }
}

export function ZoomInReact() {
  try {
    (window as any).javaConnector.ZoomInReactCall();
  } catch (err) {
    ErrorMessage("ZoomInReact", "", err);
  }
}

export function ZoomOutReact() {
  try {
    (window as any).javaConnector.ZoomOutReactCall();
  } catch (err) {
    ErrorMessage("ZoomOutReact", "", err);
  }
}
