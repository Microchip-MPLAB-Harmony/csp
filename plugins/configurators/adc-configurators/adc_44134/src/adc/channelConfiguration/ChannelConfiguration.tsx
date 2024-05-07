import React, { useState, useContext } from "react";
import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";
import {
  PluginConfigContext,
  createClassResolver,
  DropDown,
  useKeyValueSetSymbol,
  useCommentSymbol,
} from "@mplab_harmony/harmony-plugin-client-lib";
import ChannelConfigurationTable from "./ChannelConfigurationTable";
import positions from "../../styles/positions.module.css";

const cx = createClassResolver(positions);
const ChannelConfiguration = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const [channelConfigPopup, setChannelConfigPopup] = useState(false);

  const resultResolution = useKeyValueSetSymbol({
    componentId,
    symbolId: "ADC_EMR_OSR_VALUE",
  });
  const conversionTime = useCommentSymbol({
    componentId,
    symbolId: "ADC_CONV_TIME",
  });

  return (
    <>
      <DropDown
        keyValueSetSymbolHook={resultResolution}
        className={cx("resultResolution")}
      ></DropDown>
      <Button
        label="Channel Configuration"
        className={cx("channelConfigButton")}
        onClick={() => {
            setChannelConfigPopup(!channelConfigPopup);
        }}
      />
      <label className={cx("conversionTime")}>{conversionTime?.label
                ?.replace("**** Conversion Time is ", "")
                ?.replace(" ****", "")}</label>
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
