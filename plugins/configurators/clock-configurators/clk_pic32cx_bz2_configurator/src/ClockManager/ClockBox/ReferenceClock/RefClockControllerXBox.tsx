import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import RefClkControllerBoxTemplate from './RefClockControllerBoxTemplate';
import { getRefClkSettingsSymbol } from './RefClockSettingsSymbol';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import RefClockFrequency from './RefClockFrequency';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';
import { getDynamicLabelsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';

interface Tab {
  name: string;
  index: string;
  status: string;
}

export const refClkTabs: Tab[] = [
  { name: 'REFCLK 1', index: '1', status: 'CONFIG_SYS_CLK_REFCLK1_ENABLE' },
  { name: 'REFCLK 2', index: '2', status: 'CONFIG_SYS_CLK_REFCLK2_ENABLE' },
  { name: 'REFCLK 3', index: '3', status: 'CONFIG_SYS_CLK_REFCLK3_ENABLE' },
  { name: 'REFCLK 4', index: '4', status: 'CONFIG_SYS_CLK_REFCLK4_ENABLE' },
  { name: 'REFCLK 5', index: '5', status: 'CONFIG_SYS_CLK_REFCLK5_ENABLE' },
  { name: 'REFCLK 6', index: '6', status: 'CONFIG_SYS_CLK_REFCLK6_ENABLE' }
];

const RefClockControllerXBox = (props: {
  refClockData: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [value, setValue] = useState<Tab | null>(refClkTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const refClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '10px' }}
        className={refClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  const [dynamicLabelSymbolsInfo] = useState(() => getDynamicLabelsFromJSON(props.refClockData));

  return (
    <div>
      <div>
        <ListBox
          className={props.cx('refClkTab')}
          value={value}
          options={refClkTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <RefClkControllerBoxTemplate
        index={value?.name ? value.index : '1'}
        RefClkSettingsSymbolArray={getRefClkSettingsSymbol(value?.name ? value.index : '1')}
        RefClkController={props.refClockData}
        componentId={componentId}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolsInfo}
        cx={props.cx}
      />
      <RefClockFrequency
        cx={props.cx}
        componentId={componentId}
      />
    </div>
  );
};
export default RefClockControllerXBox;
