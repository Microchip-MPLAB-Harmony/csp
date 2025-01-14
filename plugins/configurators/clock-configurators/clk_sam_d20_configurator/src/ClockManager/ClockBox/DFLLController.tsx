import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { useContext, useState } from 'react';
import { removeDuplicates } from 'clock-common/lib/Tools/Tools';
import SettingsDialog from 'clock-common/lib/Components/SettingsDialog';
import {
  configSymbolApi,
  KeyValueSetRadio,
  PluginConfigContext,
  useBooleanSymbol,
  useIntegerSymbol,
  useKeyValueSetSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import ResetSymbolsIcon from 'clock-common/lib/Components/ResetSymbolsIcon';
import { GetButton } from 'clock-common/lib/Components/NodeType';
import { Dialog } from 'primereact/dialog';
import LoadDynamicComponents from 'clock-common/lib/Components/Dynamic/LoadDynamicComponents';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import {
  getDynamicLabelsFromJSON,
  getDynamicSymbolsFromJSON
} from 'clock-common/lib/Tools/ClockJSONTools';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';

let dfllSettingsSymbolArray = [
  'CONFIG_CLOCK_DFLL_ENABLE',
  'CONFIG_CLOCK_DFLL_OPMODE',
  'CONFIG_CLOCK_DFLL_ONDEMAND',
  'CONFIG_CLOCK_DFLL_QUICK_LOCK',
  'CONFIG_CLOCK_DFLL_CHILL_CYCLE',
  'CONFIG_CLOCK_DFLL_LLAW',
  'CONFIG_CLOCK_DFLL_STABLE',
  'CONFIG_CLOCK_DFLL_COARSE',
  'CONFIG_CLOCK_DFLL_FINE',
  'CONFIG_CLOCK_DFLL_MUL'
];

const DFLLController = (props: {
  dfllControllerData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [dialogStatus, setDialogStatus] = useState(false);
  const dfllOPMode = useKeyValueSetSymbol({ componentId, symbolId: 'CONFIG_CLOCK_DFLL_OPMODE' });
  const CONFIG_CLOCK_DFLL_MUL = useIntegerSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DFLL_MUL'
  });
  const dfllEnable = useBooleanSymbol({ componentId, symbolId: 'CONFIG_CLOCK_DFLL_ENABLE' });
  const dfllOperationMode = useKeyValueSetSymbol({
    componentId,
    symbolId: 'CONFIG_CLOCK_DFLL_OPMODE'
  });
  const GCLK_ID_0_FREQ = useIntegerSymbol({ componentId, symbolId: 'GCLK_ID_0_FREQ' });

  let symbols: any = props.dfllControllerData
    .map((e) => e.symbol_id)
    .filter((e) => e !== undefined);
  symbols = symbols.concat(dfllSettingsSymbolArray);
  symbols = removeDuplicates(symbols);

  const [dynamicSymbolsInfo] = useState(() => getDynamicSymbolsFromJSON(props.dfllControllerData));
  const [dynamicLabelSymbolInfo] = useState(() =>
    getDynamicLabelsFromJSON(props.dfllControllerData)
  );

  const autoCalculateAction = () => {
    if (!dfllEnable.value) {
      setDialogStatus(true);
      return;
    }
    let nDesiredOutputFreq = 48000000;
    let nRefFrequency = GCLK_ID_0_FREQ.value;
    let nMulValue = nDesiredOutputFreq / nRefFrequency;
    configSymbolApi.setValue(componentId, 'CONFIG_CLOCK_DFLL_MUL', Number(nMulValue));
  };

  return (
    <div>
      <LoadDynamicComponents
        componentId={componentId}
        dynamicSymbolsInfo={dynamicSymbolsInfo}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        redColorForZeroFrequency={true}
        cx={props.cx}
      />
      <PlainLabel
        disPlayText={CONFIG_CLOCK_DFLL_MUL.value + ''}
        className={props.cx('dfllDivLabel')}
      />
      <KeyValueSetRadio
        keyValueSetSymbolHook={dfllOPMode}
        classResolver={props.cx}
        classPrefix={'dfllRefClockRadio'}
      />

      <SettingsDialog
        tooltip='DFLL Configuration'
        componentId={componentId}
        className={props.cx('dfll_settings')}
        symbolArray={dfllSettingsSymbolArray}
        dialogWidth='55rem'
        dialogHeight='40rem'
      />
      <ResetSymbolsIcon
        tooltip='Reset DFLL symbols to default value'
        className={props.cx('dfll_reset')}
        componentId={componentId}
        resetSymbolsArray={symbols}
      />
      {dfllOperationMode.selectedOption === 'Closed' && (
        <GetButton
          buttonDisplayText={'Auto Calculate'}
          className={props.cx('dfll_AutoCalculate')}
          toolTip={'DFLL Auto Settings Calculation'}
          buttonClick={() => {
            autoCalculateAction();
          }}
        />
      )}
      <Dialog
        header={'DFLL Auto Settings Calculation'}
        visible={dialogStatus}
        style={{ width: '30rem', height: '15rem' }}
        maximizable={true}
        onHide={() => {
          setDialogStatus(false);
        }}>
        <div>Please Enable DFLL</div>
      </Dialog>
    </div>
  );
};
export default DFLLController;
