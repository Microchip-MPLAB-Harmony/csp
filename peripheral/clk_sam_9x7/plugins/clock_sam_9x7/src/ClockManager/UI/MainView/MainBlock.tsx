import ClockSVG from "../../../Resources/Svgs/SAM9X7_clock.svg";
import myData from "../../../Resources/Json/symbol.json";
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
import { AddCustomLabels } from "./CustomLabels";
import { AddCustomButtons } from "./CustomButtons";
import TabbedButton from "./ProgrammableClockController";
import SummaryPage from "./Summary";

let symbolsStyle = new Map<any, any>();
export let component_id = "core";
export let toolBarHeight = "60px";
let symbolsArray: string[] = [];
let labelsArray: string[] = [];

let dynamicSymbolsIgnoreList = [
  "CLK_PCK0_CSS",
  "CLK_PCK0_PRES",
  "CLK_PCK0_EN",
  "CLK_PCK0_FREQUENCY",
];

const MainBlock = () => {
  const update = useForceUpdate();

  function UpdateScreen() {
    update();
  }

  function AddNonSymbolLinkedLabels() {
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

  function AddSymbolLinkedUIComponents() {
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

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card" id="motor">
        <img
          src={ClockSVG}
          alt="icon"
          style={{ width: "1300px", height: "1740px", top: "0px", left: "0px" }}
        />
        {AddSymbolLinkedUIComponents()}
        {AddNonSymbolLinkedLabels()}
        {AddCustomLabels()}
        {AddCustomButtons()}
        <TabbedButton parentUpdate={UpdateScreen} />
      </div>
      <div id="summary" style={{ display: "none" }}>
        <SummaryPage />{" "}
      </div>
    </div>
  );
};

export default MainBlock;

export function ReadJSONData() {
  symbolsArray.length = 0;
  labelsArray.length = 0;
  globalSymbolStyleData.clear();
  let symbolsData: any = myData;
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
