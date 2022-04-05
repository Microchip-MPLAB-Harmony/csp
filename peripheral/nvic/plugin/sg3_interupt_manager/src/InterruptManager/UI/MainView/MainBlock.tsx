import useForceUpdate from "use-force-update";
import Headder from "./ToolBar";
import { SetComponentId } from '../../Common/SymbolAccess';
import InterruptTable from "./InterruptTable";
import { DisaableProgress } from './Progress';

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

  return (
    <div>
      <div>
        <Headder />
      </div>
      <div className="card">
      <div  id="motor">
        <InterruptTable parentUpdate={UpdateScreen} />
      </div>
      {/* {DisaableProgress()} */}
      </div>
    </div>
  );
};

export default MainBlock;
