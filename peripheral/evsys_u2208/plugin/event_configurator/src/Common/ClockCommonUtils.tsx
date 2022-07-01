import {
  GetStyle,
  GetMinFractionValueBasedSymbolType,
  globalSymbolStyleData,
} from "./UIComponents/UIComponentCommonUtils";
import { component_id } from "../EventConfigurator/UI/MainView/MainBlock";
import {
  GetSymbolArray,
  GetSymbolMaxValue,
  GetSymbolMinValue,
  GetSymbolValue,
} from "./SymbolAccess";
import { InputNumber as PrimeInputNumber } from "primereact/inputnumber";
import { Checkbox as PrimeCheckbox } from "primereact/checkbox";
import { GetSymbolReadOnlyStatus } from "./SymbolAccess";
import CheckBox from "./UIComponents/CheckBox";
import DropDown from "./UIComponents/DropDown";
import InputNumber from "./UIComponents/InputNumber";
import {
  GetLabelWithCustomDisplay,
  GetLabelWithCustomDisplayWithTooltip,
} from "./UIComponents/Label";

function GetColoredStyleObject(id: string, isValidFreq: boolean) {
  try {
    let style: any = globalSymbolStyleData.get(id);
    if (style !== undefined) {
      if (isValidFreq === true) {
        style.set("color", "black");
      } else {
        style.set("color", "red");
      }
    }
    return Object.fromEntries(style);
  } catch (err) {}
}

export function AddBoldLabel(
  id: string,
  text: string,
  symbolSelectionStatus: boolean
) {
  try {
    let style: Map<string, string> | undefined = globalSymbolStyleData.get(id);
    if (style !== undefined) {
      if (symbolSelectionStatus === true) {
        style.set("font-weight", "bold");
      } else {
        style.set("font-weight", "normal");
      }
    }
    return <div>{AddLabelWithCustomStyle(id, text, style)}</div>;
  } catch (err) {}
}

function AddLabelWithCustomStyle(id: string, text: string, styleMap: any) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={id}
          labelDisplayText={text}
          labelStyle={Object.fromEntries(styleMap)}
        />
      </div>
    );
  } catch (err) {}
}

export function AddFrequencyLabel(symbolId: string, styleId: string) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + " Hz"}
          labelStyle={GetStyle(styleId)}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddFrequencyLabelWithBold(
  symbolId: string,
  styleId: string,
  symbolSelectionStatus: boolean
) {
  try {
    let style: any = globalSymbolStyleData.get(styleId);
    if (style !== undefined) {
      if (symbolSelectionStatus === true) {
        style.set("font-weight", "bold");
      } else {
        style.set("font-weight", "normal");
      }
    }
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + " Hz"}
          labelStyle={Object.fromEntries(style)}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddColoredFrequencyLabel(
  symbolId: string,
  styleId: string,
  isValidFrequency: boolean
) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + " Hz"}
          labelStyle={GetColoredStyleObject(styleId, isValidFrequency)}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddColoredFrequencyLabelWithTooltip(
  symbolId: string,
  styleId: string,
  isValidFrequency: boolean,
  tooltip: string
) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplayWithTooltip
          labelId={symbolId}
          labelDisplayText={GetSymbolValue(component_id, symbolId) + " Hz"}
          labelStyle={GetColoredStyleObject(styleId, isValidFrequency)}
          labelTooltip={tooltip}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddCombobox(
  symbolId: string,
  styleId: string,
  parentUpdate: any
) {
  try {
    return (
      <div>
        <DropDown
          componentId={component_id}
          symbolId={symbolId}
          onChange={parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolArray={GetSymbolArray(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          className={null}
          symbolListeners={[styleId]}
          visible={true}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddCheckBox(
  symbolId: string,
  styleId: string,
  parentUpdate: any
) {
  try {
    return (
      <div>
        <CheckBox
          componentId={component_id}
          symbolId={symbolId}
          onChange={parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          className={null}
          symbolListeners={[symbolId]}
          visible={true}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddInputNumber(
  symbolId: string,
  styleId: string,
  visibleStatus: boolean,

  parentUpdate: any
) {
  try {
    return (
      <div>
        <InputNumber
          componentId={component_id}
          symbolId={symbolId}
          onChange={parentUpdate}
          symbolValue={GetSymbolValue(component_id, symbolId)}
          symbolListeners={[styleId]}
          minFractionValue={GetMinFractionValueBasedSymbolType(
            component_id,
            symbolId
          )}
          minValue={GetSymbolMinValue(component_id, symbolId)}
          maxValue={GetSymbolMaxValue(component_id, symbolId)}
          readOnly={GetSymbolReadOnlyStatus(component_id, symbolId)}
          styleObject={GetStyle(styleId)}
          className={null}
          visible={visibleStatus}
        />
      </div>
    );
  } catch (err) {
    alert(err);
  }
}

export function AddLabel(id: string, text: string) {
  try {
    return (
      <div>
        <GetLabelWithCustomDisplay
          labelId={id}
          labelDisplayText={text}
          labelStyle={GetStyle(id)}
        />
      </div>
    );
  } catch (err) {}
}

export function AddDivpmcType(id: string, text: string) {
  try {
    let newvalue = "(2*(" + text + "+1))";
    return <div>{AddLabel(id, "/ " + newvalue)}</div>;
  } catch (err) {}
}

export function AddDivioType(id: string, text: string) {
  try {
    let newvalue = "(" + text + "+1)";
    return <div>{AddLabel(id, "/ " + newvalue)}</div>;
  } catch (err) {}
}

export function AddDummyInputNumber(styleId: string) {
  return (
    <div>
      <PrimeInputNumber value={0} disabled style={GetStyle(styleId)} />
    </div>
  );
}

export function AddDummyCheckBox(styleId: string) {
  return (
    <div>
      <PrimeCheckbox value={false} disabled style={GetStyle(styleId)} />
    </div>
  );
}
