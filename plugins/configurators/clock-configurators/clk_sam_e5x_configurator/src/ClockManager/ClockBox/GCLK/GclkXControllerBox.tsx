import { useContext, useEffect, useState } from 'react';
import ControlInterface from 'clock-common/lib/Tools/ControlInterface';

import { ListBox } from 'primereact/listbox';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import { getGclockSymbols } from './GclkSymbols';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';
import { updateSVG } from '../../SVGHandler';

interface Tab {
  name: string;
  id: string;
  status: string;
}

const generateClkGenTabs = (maxClkGen: number): Tab[] => {
  const refClkTabs: Tab[] = [];
  for (let i = 2; i < maxClkGen; i++) {
    refClkTabs.push({
      name: `GCLK ${i}`,
      id: `${i}`,
      status: `GCLK_INST_NUM${i}`
    });
  }
  return refClkTabs;
};
const GCLKTabs = generateClkGenTabs(12);

const GclkXControllerBox = (props: {
  controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);

  const [value, setValue] = useState<Tab | null>(GCLKTabs[0]);

  useEffect(() => {
    if (value?.id === '8' || value?.id === '9' || value?.id === '10' || value?.id === '11' ) {
      updateSVG(true);
    } else {
      updateSVG(false);
    }
  }, [value]);

  const tabTemplate = (option: any) => {
    // eslint-disable-next-line react-hooks/rules-of-hooks
    const GCLKClocKEnable = useBooleanSymbol({
      componentId,
      symbolId: option.status
    });
    return (
      <div
        style={{ fontSize: '11px' }}
        className={GCLKClocKEnable.value ? props.cx('enable') : props.cx('disable')}>
        {option.name}
      </div>
    );
  };
  return (
    <div>
      <div>
        <ListBox
          className={props.cx('gclkXgenTab')}
          value={value}
          options={GCLKTabs}
          optionLabel='name'
          itemTemplate={tabTemplate}
          onChange={(e) => setValue(e.value)}
        />
      </div>
      <GCKLClockControllerBoxTemplate
        tabTitle={value?.name ? value.id : '2'}
        gclkSettingsSymbolArray={getGclockSymbols(value?.name ? value.id : '2')}
        gclkController={props.controller}
        componentId={componentId}
        cx={props.cx}
        gclKsettingsClassName={'gclkGenX_settings'}
        gclkresetClassName={'gclkGenXReset'}
        gclKinputNumberClassName={'gclkGenXDiv'}
        gclkEnableClassName={'gclkGenXEnable'}
        gclkFrequencyClassName={'gclkGenXFreq'}
        gclkDivLabelClassName={'gclkGenXDivLabel'}
        gclkRadioName='gclkGenXRadio'
        gclkRadioLabelName='gclkGenXRadioName'
      />
    </div>
  );
};
export default GclkXControllerBox;
