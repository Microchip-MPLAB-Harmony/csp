import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { getGclockSymbols } from './GclkSymbols';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';
import { useContext } from 'react';
import { PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';

const Gclk0ControllerBox = (props: {
  gclk0Controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  return (
    <div>
      <GCKLClockControllerBoxTemplate
        tabTitle={'0'}
        gclkSettingsSymbolArray={getGclockSymbols('0')}
        gclkController={props.gclk0Controller}
        componentId={componentId}
        cx={props.cx}
        gclKsettingsClassName={'gclkGen0_settings'}
        gclkresetClassName={'gclkGen0Reset'}
        gclKinputNumberClassName={'gclkGen0Div'}
        gclkEnableClassName={'gclkGen0Enable'}
        gclkFrequencyClassName={'gclkGen0Freq'}
        gclkDivLabelClassName={'gclkGen0DivLabel'}
        gclkRadioName='gclkGen0Radio'
        gclkRadioLabelName='gclkGen0RadioName'
      />
    </div>
  );
};
export default Gclk0ControllerBox;
