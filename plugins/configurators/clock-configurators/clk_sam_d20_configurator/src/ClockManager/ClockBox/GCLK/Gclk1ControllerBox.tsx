import ControlInterface from 'clock-common/lib/Tools/ControlInterface';
import { getGclockSymbols } from './GclkSymbols';
import { PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext } from 'react';
import GCKLClockControllerBoxTemplate from './GCKLClockControllerBoxTemplate';

const Gclk1ControllerBox = (props: {
  gclk1Controller: ControlInterface[];
  cx: (...classNames: string[]) => string;
}) => {
  const { componentId = 'core' } = useContext(PluginConfigContext);
  return (
    <div>
      <GCKLClockControllerBoxTemplate
        tabTitle={'1'}
        gclkSettingsSymbolArray={getGclockSymbols('1')}
        gclkController={props.gclk1Controller}
        componentId={componentId}
        cx={props.cx}
        gclKsettingsClassName={'gclkGen1_settings'}
        gclkresetClassName={'gclkGen1Reset'}
        gclKinputNumberClassName={'gclkGen1Div'}
        gclkEnableClassName={'gclkGen1Enable'}
        gclkFrequencyClassName={'gclkGen1Freq'}
        gclkDivLabelClassName={'gclkGen1DivLabel'}
        gclkRadioName='gclkGen1Radio'
        gclkRadioLabelName='gclkGen1RadioName'
      />
    </div>
  );
};
export default Gclk1ControllerBox;
