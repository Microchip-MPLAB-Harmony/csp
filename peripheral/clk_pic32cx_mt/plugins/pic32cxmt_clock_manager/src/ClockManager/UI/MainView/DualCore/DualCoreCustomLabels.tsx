import { GetSymbolValue } from "../../../Common/SymbolAccess";
import { component_id } from "../MainBlock";
import {
  AddFrequencyLabelWithBold,
  AddLabel,
} from "../../../Common/ClockCommonUtils";

export function AddDualCoreCustomLabels() {
  try {
    return (
      <div>
        {AddDiv(
          "label_core0PresValue",
          GetSymbolValue(component_id, "CLK_CPU_CKR_PRES")
        )}
        {AddDiv(
          "label_core1CPPRES",
          GetSymbolValue(component_id, "CLK_CPU_CKR_CPPRES")
        )}

        {/* Core 0 symbols*/}
        {AddFrequencyLabelWithBold(
          "MD_SLOW_CLK_FREQUENCY",
          "label_core0MdclockFreq",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "MD_SLOW_CLK")
        )}
        {AddFrequencyLabelWithBold(
          "MAINCK_FREQUENCY",
          "label_core0MainClkFrequency",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "MAINCK")
        )}
        {AddFrequencyLabelWithBold(
          "PLLACK1_FREQUENCY",
          "label_core0PLLACK1",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "PLLACK1")
        )}
        {AddFrequencyLabelWithBold(
          "PLLBCK_FREQUENCY",
          "label_core0PLLBCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CSS", "PLLBCK")
        )}
         {AddCoreDiv("CLK_CPU_CKR_RATIO_MCK0DIV", "label_core0MCK0DIVValue" )}
         {AddCoreDiv("CLK_CPU_CKR_RATIO_MCK0DIV2", "label_core0MCK0DIV2Value" )}

         {/* Core 1 symbols*/}
        {AddFrequencyLabelWithBold(
          "MD_SLOW_CLK_FREQUENCY",
          "label_core1MdclockFreq",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CPCSS", "MD_SLOW_CLK")
        )}
        {AddFrequencyLabelWithBold(
          "MAINCK_FREQUENCY",
          "label_core1MainClkFrequency",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CPCSS", "MAINCK")
        )}
        {AddFrequencyLabelWithBold(
          "PLLACK1_FREQUENCY",
          "label_core1PLLACK1",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CPCSS", "PLLACK1")
        )}
        {AddFrequencyLabelWithBold(
          "PLLBCK_FREQUENCY",
          "label_core1PLLBCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CPCSS", "PLLBCK")
        )}
        {AddFrequencyLabelWithBold(
          "PLLCCK_FREQUENCY",
          "label_core1PLLCCK",
          CheckSelectedSymbolValue("CLK_CPU_CKR_CPCSS", "PLLCCK")
        )}
         {AddCoreDiv("CLK_CPU_CKR_RATIO_MCK1DIV", "label_core1MCK1Div" )}
       
      </div>
    );
  } catch (err) {}
}

function AddCoreDiv(symoblid : string, styleId: string){
  try {
    let divStatus = GetSymbolValue(component_id, symoblid);
    
    let labelValue = "1";
    if(divStatus === "true"){
      labelValue = "2";
    }
    
    return <div>{AddLabel(styleId, "/ "+labelValue)}</div>;
  } catch (err) {}
}

export function CheckSelectedSymbolValue(symbolId: string, checkValue: string) {
  if (GetSymbolValue(component_id, symbolId) === checkValue) {
    return true;
  } else {
    return false;
  }
}

function AddDiv(id: string, text: string) {
  try {
    let divValue = RemoveDiv(text);
    divValue = divValue.replace("DIV", "");
    return <div>{AddLabel(id, "/ " + divValue)}</div>;
  } catch (err) {}
}

function RemoveDiv(value: string) {
  let newValue = value.split("_");
  return newValue[1];
}
