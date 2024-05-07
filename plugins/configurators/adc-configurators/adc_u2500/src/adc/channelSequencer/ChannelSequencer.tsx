import React, { useState } from "react";
import { Dialog } from "primereact/dialog";
import { Button } from "primereact/button";
import {
  CheckBox,
  createClassResolver,
} from "@mplab_harmony/harmony-plugin-client-lib";
import SequencerTable from "./SequencerTable";
import positions from "../../styles/positions.module.css";
import useChannelSequencerSymbols from "./useChannelSequencerSymbols";

const cx = createClassResolver(positions);
const ChannelSequencer = () => {
  const [channelSequencePopup, setChannelSequencePopup] = useState(false);
  const { isChannelSequencer } = useChannelSequencerSymbols();

  return (
    <>
      <CheckBox
        booleanSymbolHook={isChannelSequencer}
        className={cx("sequencerCheck")}
      ></CheckBox>
      <Button
        label="Channel Sequence"
        className={cx("sequence")}
        disabled={!isChannelSequencer.value}
        onClick={() => {
          setChannelSequencePopup(!channelSequencePopup);
        }}
      />
      <Dialog
        header="Channel Sequence Configuration"
        visible={channelSequencePopup}
        maximizable={true}
        onHide={() => {
          setChannelSequencePopup(!channelSequencePopup);
        }}
      >
        <SequencerTable />
      </Dialog>
    </>
  );
};

export default React.memo(ChannelSequencer);
