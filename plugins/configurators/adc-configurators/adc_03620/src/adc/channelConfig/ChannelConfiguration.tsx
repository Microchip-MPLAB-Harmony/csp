import React, { useState } from "react";
import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";
import { createClassResolver } from "@mplab_harmony/harmony-plugin-client-lib";
import ChannelConfigurationTable from "./ChannelConfigurationTable";
import positions from "../../styles/positions.module.css";
type Props = {
  moduleId: number;
};
const cx = createClassResolver(positions);
const ChannelConfiguration = ({ moduleId }: Props) => {
  const [channelConfigPopup, setChannelConfigPopup] = useState(false);

  return (
    <>
      <Button
        label="Channel Configuration"
        className={cx("channelConfigButton")}
        onClick={() => {
          setChannelConfigPopup(!channelConfigPopup);
        }}
      />

      <Dialog
        header={`Channel Configuration ADC CORE ${moduleId}`}
        visible={channelConfigPopup}
        maximizable={true}
        onHide={() => {
          setChannelConfigPopup(!channelConfigPopup);
        }}
      >
        <ChannelConfigurationTable moduleId={moduleId} />
      </Dialog>
    </>
  );
};

export default React.memo(ChannelConfiguration);
