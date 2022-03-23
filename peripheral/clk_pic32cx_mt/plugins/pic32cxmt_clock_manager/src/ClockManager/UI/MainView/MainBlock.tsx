import DualCoreClockSVG from "../../../Resources/Svgs/cleaned_PIC32CXMT_clock_dual_core.svg";
import DualCoreJsonData from "../../../Resources/Json/symbol.json";
import SingleCoreJsonData from "../../../Resources/Json/symbol.json";
import useForceUpdate from "use-force-update";
import {
  GetUIComponentWithOutLabel,
  StoreSymbolStyle,
} from "../../Common/UIComponent";
import Headder from "./ToolBar";
import {
  globalSymbolStyleData,
  GetLabelWithCustomDisplay,
  GetStyle,
} from "../../Common/UIComponent";
import { GetSymbolValue } from "../../Common/SymbolAccess";
import PCKxController from "./Tabs/ProgrammableClockController";
import PLLController from "./Tabs/PLLController";
import { AddCustomButtons } from "./CustomButtons";
import { AddDualCoreCustomLabels } from "./DualCore/DualCoreCustomLabels";
import SummaryPage from './Summary';

let symbolsStyle = new Map<any, any>();
export let component_id = "core";
export let toolBarHeight = "60px";
let symbolsArray: string[] = [];
let labelsArray: string[] = [];

let dynamicSymbolsIgnoreList: string | string[] = [];

let SelectedCore = GetSymbolValue(component_id, "CoreSeries");
let DualCoreSeries = ["PIC32CXMTC", "PIC32CXMTSH"];
let SingleCoreSeries = ["PIC32CXMTG"];
export let dualCoreString = "DualCore";
export let singleCoreString = "SingleCore";

export function GetCoreStatus() {
  if (DualCoreSeries.includes(SelectedCore)) {
    return dualCoreString;
  } else if (SingleCoreSeries.includes(SelectedCore)) {
    return singleCoreString;
  }
  return singleCoreString;
}

const MainBlock = () => {
  const update = useForceUpdate();

  function timeout(delay: number) {
    return new Promise((res) => setTimeout(res, delay));
  }
  async function UpdateScreen() {
    await timeout(200);
    update();
  }

  function AddDynamicNonSymbolLinkedLabels() {
    try {
      return (
        <div className="p-fluid">
          {labelsArray.map((id: string) => (
            <GetLabelWithCustomDisplay
              labelId={id}
              labelDisplayText={GetSymbolValue(component_id, id) + " Hz"}
              labelStyle={GetStyle(id)}
            />
          ))}
        </div>
      );
    } catch (err) {}
  }

  function AddDynamicSymbolLinkedUIComponents() {
    try {
      return (
        <div className="p-fluid">
          {symbolsArray.map((id: string) => (
            <GetUIComponentWithOutLabel
              componentId={component_id}
              symbolId={id}
              onChange={UpdateScreen}
            />
          ))}
        </div>
      );
    } catch (err) {}
  }

  function LoadDualCoreSVG() {
    return (
      <div>
        <img
          src={DualCoreClockSVG}
          alt="icon"
          style={{ width: "1764px", height: "1548px", top: "0px", left: "0px" }}
        />
        {AddDualCoreCustomLabels()}
      </div>
    );
  }

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card"  id="motor">
        {GetCoreStatus() === dualCoreString && LoadDualCoreSVG()}
        {AddDynamicSymbolLinkedUIComponents()}
        {AddDynamicNonSymbolLinkedLabels()}
        {AddCustomButtons()}
        <PCKxController parentUpdate={UpdateScreen} />
        <PLLController parentUpdate={UpdateScreen} />
      </div>
      <div id="summary" style={{ display: "none" }}>
        {" "}
        <SummaryPage />{" "}
      </div>
    </div>
  );
};

export default MainBlock;

export function ReadJSON() {
  if (GetCoreStatus() === dualCoreString) {
    ReadJSONData(DualCoreJsonData);
  } else if (GetCoreStatus() === singleCoreString) {
    ReadJSONData(SingleCoreJsonData);
  }
}

function ReadJSONData(jsondata: any) {
  symbolsArray.length = 0;
  labelsArray.length = 0;
  globalSymbolStyleData.clear();
  let symbolsData: any = jsondata;
  for (let prop in symbolsData) {
    let settings = symbolsData[prop];
    if (prop.startsWith("sym_")) {
      prop = prop.replace("sym_", "");
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        symbolsArray.push(prop);
      }
    } else if (prop.startsWith("label_sym_")) {
      prop = prop.replace("label_sym_", "");
      if (!dynamicSymbolsIgnoreList.includes(prop)) {
        labelsArray.push(prop);
      }
    }
    for (let temp in settings) {
      symbolsStyle.set(prop, settings[temp]);
    }
    StoreSymbolStyle(prop, symbolsStyle);
  }
}
