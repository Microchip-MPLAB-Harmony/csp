import { useContext, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import MCKClkControllerBoxTemplate from './MCKClockControllerBoxTemplate';
import { PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import { getMckClkSettingsSymbol } from './MCKClockSettingsSymbol';
import FreqencyLabels from 'clock-common/lib/Components/LabelComponent/FreqencyLabels';
import { getDynamicLabelsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';

interface Tab {
  name: string;
  id: string;
}

export const mckTabs: Tab[] = [
  { name: 'MCK 1', id: '1' },
  { name: 'MCK 2', id: '2' },
  { name: 'MCK 3', id: '3' },
  { name: 'MCK 4', id: '4' },
  { name: 'MCK 5', id: '5' },
  { name: 'MCK 6', id: '6' },
  { name: 'MCK 7', id: '7' },
  { name: 'MCK 8', id: '8' },
  { name: 'MCK 9', id: '9' }
];

const MCKClockControllerXBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(mckTabs[0]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks

    return <div style={{ fontSize: '10px' }}>{option.name}</div>;
  };
  const [dynamicLabelSymbolInfo] = useState(() => getDynamicLabelsFromJSON(props.controller));
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('mckTab')}
          value={value}
          options={mckTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <MCKClkControllerBoxTemplate
        tabTitle={value?.name ? value.id : '1'}
        clkSettingsSymbolArray={getMckClkSettingsSymbol(value?.name ? value.id : '1')}
        clkController={props.controller}
        componentId={componentId}
        cx={props.cx}
      />
      <FreqencyLabels
        componentId={componentId}
        boxInfo={dynamicLabelSymbolInfo}
        cx={props.cx}
      />
    </div>
  );
};
export default MCKClockControllerXBox;
