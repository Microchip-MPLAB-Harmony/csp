import { createClassResolver, PluginConfigContext } from '@mplab_harmony/harmony-plugin-client-lib';
import { useContext, useState } from 'react';
import { getBoxControlData } from '../MainBlock';
import { getAllSymbolsFromJSON } from 'clock-common/lib/Tools/ClockJSONTools';
import style from './summary.module.css';
import { Accordion, AccordionTab } from 'primereact/accordion';
import { Fieldset } from 'primereact/fieldset';
import { getGclockSymbols } from '../ClockBox/GCLK/GclkSymbols';
import { GCLKTabs } from '../ClockBox/GCLK/GclkXControllerBox';
import PeripheralsConfiguration from '../ClockBox/PopUp/GclockIOConfiguration';
import GenericClockConfiguration from '../ClockBox/PopUp/PeripheralClockConfiguration';
import SummaryMultipleSymbols from 'clock-common/lib/Components/SummaryMultipleSymbols';
const Summary = () => {
  const cx = createClassResolver(style);
  const { componentId = 'core' } = useContext(PluginConfigContext);
  const [oscillator8Mhz] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('8_48MhzOScillatorBox'))
  );
  const [dfllClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('dfllBox'))
  );
  const [pllClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('pllControlBox'))
  );
  const [Oscillator32KhzClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('32KhzOscillatorBox'))
  );
  const [mainClockSymbols] = useState<string[]>(
    getAllSymbolsFromJSON(getBoxControlData('mainClkBox'))
  );

  return (
    <div>
      <Accordion
        activeIndex={0}
        style={{ width: '80vw' }}>
        <AccordionTab header='8-48 MHz Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={oscillator8Mhz.concat('XOSC_OSCILLATOR_MODE')}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='DFLL Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={dfllClockSymbols.concat('CONFIG_CLOCK_DFLL_OPMODE')}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='Phase Locked Loop Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={pllClockSymbols}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='32 KHz Oscillator Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={Oscillator32KhzClockSymbols}
            />
          </div>
        </AccordionTab>
        <AccordionTab header='GCLK 0 Clock Configuration'>
          <SummaryMultipleSymbols
            componentId={componentId}
            symbolsArray={getGclockSymbols('0')}
          />
        </AccordionTab>
        <AccordionTab header='GCLK 1 Clock Configuration'>
          <SummaryMultipleSymbols
            componentId={componentId}
            symbolsArray={getGclockSymbols('1')}
          />
        </AccordionTab>
        <AccordionTab header='GCLK X Configuration'>
          <div className={cx('summary-tab-container')}>
            {GCLKTabs.map((tab) => (
              <Fieldset legend={tab.name}>
                <div
                  key={tab.id}
                  className={cx('summary-options')}>
                  <SummaryMultipleSymbols
                    componentId={componentId}
                    symbolsArray={getGclockSymbols(tab.id)}
                  />
                </div>
              </Fieldset>
            ))}
          </div>
        </AccordionTab>
        <AccordionTab header='Main Clock Configuration'>
          <SummaryMultipleSymbols
            componentId={componentId}
            symbolsArray={mainClockSymbols}
          />
        </AccordionTab>
        <AccordionTab header='Peripheral and Generic Clock Configuration'>
          <div className={cx('summary-tab-container')}>
            <Fieldset legend={'Peripheral Clock Configuration'}>
              <div className={cx('summary-options')}>
                <PeripheralsConfiguration />
              </div>
            </Fieldset>
            <Fieldset legend={'Generic Clock Configuration'}>
              <GenericClockConfiguration />
            </Fieldset>
          </div>
        </AccordionTab>
        <AccordionTab header='RTC Clock Configuration'>
          <div>
            <SummaryMultipleSymbols
              componentId={componentId}
              symbolsArray={['CONFIG_CLOCK_RTC_SRC']}
            />
          </div>
        </AccordionTab>
      </Accordion>
    </div>
  );
};
export default Summary;
