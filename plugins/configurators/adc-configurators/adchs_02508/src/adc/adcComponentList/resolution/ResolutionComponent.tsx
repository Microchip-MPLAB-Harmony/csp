import React, { useContext } from "react";
import {
  createClassResolver,
  useKeyValueSetSymbol,
  PluginConfigContext,
  DropDown,
} from "@mplab_harmony/harmony-plugin-client-lib";
import positions from "../../../styles/positions.module.css";
type ResolutionSymbolProps = {
  resolutionSymbol: string;
};

const cx = createClassResolver(positions);
const ResolutionComponent = ({ resolutionSymbol }: ResolutionSymbolProps) => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const resolution = useKeyValueSetSymbol({
    componentId,
    symbolId: resolutionSymbol,
  });
  
  return (
    <div>
      <DropDown
        keyValueSetSymbolHook={resolution}
        className={cx("resolution")}
        disabled = {!resolution.visible} 
        hidden={false}
      ></DropDown>
    </div>
  );
};

export default ResolutionComponent;
