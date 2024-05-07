import React, { useContext, useState } from "react";
import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";
import {
  PluginConfigContext,
  createClassResolver,
  useBooleanSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import ChannelConfigurationTable from "./ChannelConfigurationTable";
import positions from "../../styles/positions.module.css";
import useSymbolControl from "./useSymbolControl";
import useADCModuleConfig from "../adcComponentList/useADCModuleConfig";

const cx = createClassResolver(positions);
const ChannelConfiguration = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [channelConfigPopup, setChannelConfigPopup] = useState(false);
  const { symbolIds } = useSymbolControl();
  const { sharedModuleId } = useADCModuleConfig();
  const channelEnable = useBooleanSymbol({
    componentId,
    symbolId: `ADCHS_${sharedModuleId}_ENABLE`,
  });
  return (
    <>
      <label className={cx("pinLabel0")}>{symbolIds[0]?.analogInput}</label>
      <label className={cx("pinLabel3")}>
        {symbolIds[symbolIds?.length - 1]?.analogInput}
      </label>
      <label className={cx("pinLabelVr0")}>VREFL</label>
      <label className={cx("pinLabelVr1")}>AN1</label>

      <Button
        label="Channel Selection"
        className={cx("channelConfig")}
        onClick={() => {
          setChannelConfigPopup(!channelConfigPopup);
        }}
        disabled={!channelEnable.value}
      />

      <Dialog
        header="Channel Configuration ADC"
        visible={channelConfigPopup}
        maximizable={true}
        onHide={() => {
          setChannelConfigPopup(!channelConfigPopup);
        }}
      >
        <ChannelConfigurationTable />
      </Dialog>
    </>
  );
};

export default React.memo(ChannelConfiguration);
