import { useContext, useState } from 'react';
import { ListBox } from 'primereact/listbox';
import FDPLLControllerBoxTemplate from './FDPLLControllerBoxTemplate';
import { getFDPLLSettingsSymbol } from './FDPLLSettingsSymbol';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

interface Tab {
  name: string;
  id: string;
  status: string;
}
const newTabs: Tab[] = [
  { name: 'FDPLL 0', id: '0', status: 'CONFIG_CLOCK_DPLL0_ENABLE' },
  { name: 'FDPLL 1', id: '1', status: 'CONFIG_CLOCK_DPLL1_ENABLE' }
];

const FDPLLControllerXBox = (props: {
  fdpllData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [value, setValue] = useState<Tab | null>(newTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const fdpllEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '11px' }}
        className={fdpllEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };

  return (
    <div>
      <div>
        <ListBox
          className={props.cx('e5x_fdpllTab')}
          value={value}
          options={newTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <FDPLLControllerBoxTemplate
        index={value?.name ? value.id : '0'}
        fdpllsettingsClassName={'e5x_fdpll_settings'}
        fdpllresetClassName={'e5x_fdpll_reset'}
        fdpllClockSourceClassName={'e5x_fdpllCS'}
        fdpllEnableClassName={'e5x_fdllEnable'}
        fdplloscFdpllChannelEnableClassName={'e5x_fdpllCSEnable'}
        fdpllFrequencyClassName={'e5x_dpll96MFreq'}
        fdpllDivLabelClassName={'e5x_fdpllDivLabel'}
        fdpllDivClassName={'e5x_fdpllMul'}
        fdplldpllRefClockClassName={'e5x_fdpllMuxSel'}
        fdpll96MInputFreqClassName={'e5x_fdpll96MInputFreq'}
        fdpllLdrIntClassName={'e5x_fdpllLdrInt'}
        fdpllLdrFracClassName={'e5x_fdpllLdrFrac'}
        fdpllLdrLabelClassName={'e5x_fdpllLdrLabel'}
        fdpllAutoCalculateClassName={'e5x_fdpllAutoCalculate'}
        fdpllSettingsSymbolArray={getFDPLLSettingsSymbol(value?.name ? value.id : '0')}
        fdpllController={props.fdpllData}
        cx={props.cx}
        componentId={componentId}
      />
    </div>
  );
};
export default FDPLLControllerXBox;
