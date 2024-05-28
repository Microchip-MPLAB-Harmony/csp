import { Accordion, AccordionTab } from 'primereact/accordion';
import style from './summary.module.css';
import {
  createClassResolver,
  PluginConfigContext,
  useComboSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useState } from 'react';
import { getAllSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import { getBoxControlData } from '../MainBlock';
import SummaryMultipleSymbols from 'clock-common/lib/Components/SummaryMultipleSymbols';
import { getPLLClkSettingsSymbol } from '../ClockBox/PLLClock/PLLClockSettingsSymbol';
import { Fieldset } from 'primereact/fieldset';
import { pllTabs } from '../ClockBox/PLLClock/PLLClockControllerXBox';
import { mckTabs } from '../ClockBox/MCK/MCKClockControllerXBox';
import { getMckClkSettingsSymbol } from '../ClockBox/MCK/MCKClockSettingsSymbol';
import { pckTabs } from '../ClockBox/PCK/PCKClockControllerXBox';
import { getPckClkSettingsSymbol } from '../ClockBox/PCK/PCKClockSettingsSymbol';
import GenericClockConfigurationSummary from './GenericClockConfigurationSummary';

const Summary = () => {
  const cx = createClassResolver(style);
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [slowClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('slowClockBox'))
  );
  const [mainClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('mainClkBox'))
  );

  const [processorClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('processClockBox'))
  );
  const [usbClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('usbControlBox'))
  );
  const peripheralClkIds = useComboSymbol({
    componentId,
    symbolId: 'PERIPHERAL_CLOCK_CONFIG'
  });

  let channelPeripipheralMap = peripheralClkIds.options;
  return (
    <div>
      <Accordion
        activeIndex={0}
        style={{ width: '80vw' }}>
        <AccordionTab header='Slow Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={slowClockSymbols}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='Main Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={mainClockSymbols}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='PLL Clock Configuration'>
          <div className={cx('summary-tab-container')}>
            {pllTabs.map((tab) => (
              <Fieldset legend={tab.name}>
                <div
                  key={tab.status}
                  className={cx('summary-options')}>
                  <SummaryMultipleSymbols
                    componentId={componentId}
                    symbolsArray={getPLLClkSettingsSymbol(tab.name)}
                  />
                </div>
              </Fieldset>
            ))}
          </div>
        </AccordionTab>
        <AccordionTab header='Processor Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={processorClockSymbols}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='MCK Clock Configuration'>
          <div className={cx('summary-tab-container')}>
            {mckTabs.map((tab) => (
              <Fieldset legend={tab.name}>
                <div
                  key={tab.id}
                  className={cx('summary-options')}>
                  <SummaryMultipleSymbols
                    componentId={componentId}
                    symbolsArray={getMckClkSettingsSymbol(tab.id)}
                  />
                </div>
              </Fieldset>
            ))}
          </div>
        </AccordionTab>
        <AccordionTab header='PCK Configuration'>
          <div className={cx('summary-tab-container')}>
            {pckTabs.map((tab) => (
              <Fieldset legend={tab.name}>
                <div
                  key={tab.id}
                  className={cx('summary-options')}>
                  <SummaryMultipleSymbols
                    componentId={componentId}
                    symbolsArray={getPckClkSettingsSymbol(tab.id)}
                  />
                </div>
              </Fieldset>
            ))}
          </div>
        </AccordionTab>
        <AccordionTab header='Peripheral and Generic Clock Configuration'>
          <div className={cx('summary-tab-container')}>
            <Fieldset legend={'Peripheral Clock Configuration'}>
              <div className={cx('summary-options')}>
                <SummaryMultipleSymbols
                  componentId={componentId}
                  symbolsArray={channelPeripipheralMap}
                />
              </div>
            </Fieldset>
            <Fieldset legend={'Generic Clock Configuration'}>
              <div className={cx('summary-options')}>
                <GenericClockConfigurationSummary />
              </div>
            </Fieldset>
          </div>
        </AccordionTab>

        <AccordionTab header='USB Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={usbClockSymbols.concat('CLK_USB_USBS')}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='System Counter'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={['SYSTEM_COUNTER_ENABLE', 'SYSTEM_COUNTER_FREQUENCY']}
            />
          </div>
        </AccordionTab>
      </Accordion>
    </div>
  );
};
export default Summary;
