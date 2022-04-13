import useForceUpdate from "use-force-update";
import Headder from "./ToolBar";
import { SetComponentId, GetSymbolValue } from '../../Common/SymbolAccess';
import InterruptTable, { PriorityChanged } from "./InterruptTable";
import { DisaableProgress } from './Progress';
import { InputText } from "primereact/inputtext";
import { HideDiv } from '../../Common/NodeUtils';
import { globalSymbolSStateData } from "../../Common/UIComponents/UIComponentCommonUtils";
import { Button } from "primereact/button";

export let progressStatus = true;

export let component_id = "core";
export let toolBarHeight = "60px";

const MainBlock = () => {
  const update = useForceUpdate();

  SetComponentId(component_id);

  function timeout(delay: number) {
    return new Promise((res) => setTimeout(res, delay));
  }
  async function UpdateScreen() {
    await timeout(150);
    update();
  }

  function symbolValueChanged(){
    let symbolChange = document.getElementById("symbolChangeListner")?.getAttribute("symbolChange");
    if(symbolChange!== null && symbolChange !== undefined){
      let symbolData = symbolChange.split("M*C");
      let symbolId = symbolData[0];
      let symbolValue = symbolData[1]; 
      globalSymbolSStateData.get(symbolId).changeValue(symbolValue);
     
      if(symbolId.endsWith("_PRIORITY")){
        let nvicID = symbolId.split("_")[1]+"_";
        PriorityChanged(symbolValue, nvicID);
        
      }
    }
  }

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card">
      <div  id="motor">
        <InterruptTable parentUpdate={UpdateScreen} />
      </div>
      <div id="symbolChangeButtonid" style={{display : "none"}}>
         <Button id="symbolChangeListner" onClick={(e) => symbolValueChanged()}/>
      </div>
      {/* {HideDiv(document.getElementById("symbolChangeButtonid"))} */}
      {/* {DisaableProgress()} */}
      </div>
    </div>
  );
};

export default MainBlock;
