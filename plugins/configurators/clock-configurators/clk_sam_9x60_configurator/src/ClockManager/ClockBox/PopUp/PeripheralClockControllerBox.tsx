import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {useContext, useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import PeripheralClockConfiguration from './PeripheralClockConfiguration';
import { PluginConfigContext, useComboSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';

const PeripheralClockControllerBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [periPheralPopup, setPeriPheralPopup] = useState(false);
  const { componentId = "core" } = useContext(PluginConfigContext);
  const gclk_ids = useComboSymbol({
    componentId,
    symbolId: "PCRCLK_IO_CLOCK_CONFIG_UI",
  });
  let peripheralClockSymbolArray = createPeripheralSymbolsArray();
  function createPeripheralSymbolsArray() {
    let dataArr = [];
    for (let i = 0; i < gclk_ids.options.length; i++) {
      dataArr.push(gclk_ids.options[i] + "_CLOCK_ENABLE");
    }
    return dataArr;
  }
  return (
    <div>
      <Button
        label='Peripheral Clock Configuration'
        className={props.cx('periPheralClock')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Dialog
        header='Peripheral Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <PeripheralClockConfiguration />
      </Dialog>
      <ResetSymbolsIcon
        tooltip='Reset Peripheral Clock Configuration symbols to default value'
        className={props.cx('peripheralClockSelectionReset')}
        componentId={componentId}
        resetSymbolsArray={peripheralClockSymbolArray}
      />
    </div>
  );
};

export default PeripheralClockControllerBox;
