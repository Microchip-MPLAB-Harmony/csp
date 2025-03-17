import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import {useContext, useState } from 'react';
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import GenericClockConfig from './GenericClockConfig';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import { PluginConfigContext, useComboSymbol, useIntegerSymbol } from '@mplab_harmony/harmony-plugin-client-lib';

const GenericClockConfigBox = (props: {
  clockController: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const [periPheralPopup, setPeriPheralPopup] = useState(false);
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const gclk_ids = useComboSymbol({
    componentId,
    symbolId: "GCLK_IO_CLOCK_CONFIG_UI",
  });
  let gclkSymbolArray = createGclockSymbolArray();
  function createGclockSymbolArray() {
    let dataArr = [];
    for (let i = 0; i < gclk_ids.options.length; i++) {
      dataArr.push("CLK_" + gclk_ids.options[i] + "_GCLKEN");
      dataArr.push("CLK_" + gclk_ids.options[i] + "_GCLKCSS");
      dataArr.push("CLK_" + gclk_ids.options[i] + "_GCLKDIV");
    }
    return dataArr;
  }
  return (
    <div>
      <Button
        label='Generic Clock Configuration'
        className={props.cx('gclockConfig')}
        onClick={() => setPeriPheralPopup(true)}
      />
      <Dialog
        header='Generic Clock Configuration'
        visible={periPheralPopup}
        maximizable={true}
        onHide={() => {
          setPeriPheralPopup(false);
        }}>
        <GenericClockConfig />
      </Dialog>
      <ResetSymbolsIcon
        tooltip='Reset Generic Clock Configuration symbols to default value'
        className={props.cx('gclkIOReset')}
        componentId={componentId}
        resetSymbolsArray={gclkSymbolArray}
      />
    </div>
  );
};

export default GenericClockConfigBox;
