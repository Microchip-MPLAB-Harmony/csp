import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import PCKClkControllerBoxTemplate from './PCKClockControllerBoxTemplate';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { getPckClkSettingsSymbol } from './PCKClockSettingsSymbol';
import { getDynamicLabelsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import LoadDynamicFreqencyLabels from 'clock-common/lib/Components/Dynamic/LoadDynamicFreqencyLabels';

interface Tab {
  name: string;
  id: string;
  status: string;
}

export const pckTabs: Tab[] = [
  { name: 'PCK 0', id: '0', status: 'CLK_PCK0_EN' },
  { name: 'PCK 1', id: '1', status: 'CLK_PCK1_EN' },
  { name: 'PCK 2', id: '2', status: 'CLK_PCK2_EN' },
  { name: 'PCK 3', id: '3', status: 'CLK_PCK3_EN' },
  { name: 'PCK 4', id: '4', status: 'CLK_PCK4_EN' },
  { name: 'PCK 5', id: '5', status: 'CLK_PCK5_EN' },
  { name: 'PCK 6', id: '6', status: 'CLK_PCK6_EN' },
  { name: 'PCK 7', id: '7', status: 'CLK_PCK7_EN' }
];

const PCKClockControllerXBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(pckTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const pckClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '10px' }}
        className={pckClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.controller));
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('pckClkTab')}
          value={value}
          options={pckTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <PCKClkControllerBoxTemplate
        tabTitle={value?.name ? value.id : '0'}
        clkSettingsSymbolArray={getPckClkSettingsSymbol(value?.name ? value.id : '0')}
        clkController={props.controller}
        componentId={componentId}
        cx={props.cx}
      />
      <LoadDynamicFreqencyLabels
        componentId={componentId}
        dynamicLabelSymbolsInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
    </div>
  );
};
export default PCKClockControllerXBox;
