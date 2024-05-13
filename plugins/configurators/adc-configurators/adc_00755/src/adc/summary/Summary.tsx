import { Accordion, AccordionTab } from 'primereact/accordion';
import { Fieldset } from 'primereact/fieldset';
import styles from './summary.module.css';
import { useContext, useEffect, useState } from 'react';
import { getInputScanSymbols } from '../input-scan-configuration/InputScanConfiguration';
import {
  BooleanSymbol,
  PluginConfigContext,
  useBooleanSymbol,
  useSymbols
} from '@mplab_harmony/harmony-plugin-client-lib';
import useBlockDiagramViewModel from '../BlockDiagramViewModel';

function InputChannelScanConfiguration() {
  const { componentId = 'adc' } = useContext(PluginConfigContext);

  const { value: isScanEnabled } = useBooleanSymbol({
    componentId,
    symbolId: 'AD1CON2__CSCNA'
  });

  const [inputScanSymbols, setInputScanSymbols] = useState<string[]>([]);

  const symbols = useSymbols({
    componentId,
    symbolIds: inputScanSymbols
  }) as BooleanSymbol[];

  const activeInputs = symbols.filter((symbol) => symbol.value === true);

  useEffect(() => {
    getInputScanSymbols(componentId).then((symbols) =>
      setInputScanSymbols(symbols.map((symbol) => symbol.symbolId))
    );
  }, []);

  return (
    <div className={styles['one-summary-row']}>
      {isScanEnabled ? (
        <div className={styles.inputScanContainer}>
          {activeInputs.map(({ symbolId, label }) => (
            <span key={symbolId}>
              {label.replace('Select ', '').replace(' for Input Scan', '')}
            </span>
          ))}
        </div>
      ) : (
        <div>Input Scan is not enabled.</div>
      )}
    </div>
  );
}

function ADCConfigurationSummary() {
  const {
    clockDivider,
    clockSource,
    clockSourceInputFrequency,
    tad,
    voltageReference,
    outputFormat,
    resultBufferMode,
    enableAutoSampling,
    stopAutoSamplingAfter1stConversionSequence,
    autoSampleTime,
    conversionTriggerSource,
    interrupt,
    samplesPerInterrupt,
    stopInIdleMode,
    scanEnable,
    positiveInputA,
    negativeInputA,
    positiveInputB,
    negativeInputB,
    alternateInputSampleMode
  } = useBlockDiagramViewModel();

  return (
    <div className={styles['summary-tab-container']}>
      <Fieldset legend='Clock & Voltage Configuration'>
        <div className={styles['summary-options']}>
          <div>{clockSource.label}</div>
          <div>{clockSource.selectedOption}</div>
          <div>Clock Source Frequency</div>
          <div>
            {clockSource.options[0] === clockSource.selectedOption
              ? parseInt(clockSourceInputFrequency.value).toLocaleString()
              : '8,000,000'}{' '}
            Hz
          </div>
          <div>Clock Divider</div>
          <div>{clockDivider.value}</div>
          <div>{tad.label}</div>
          <div>{tad.value} ns</div>
          <div>Reference Voltage</div>
          <div>{voltageReference.selectedOption}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Interrupt Configuration'>
        <div className={styles['summary-options']}>
          <div>{interrupt.label}</div>
          <div>{interrupt.value ? 'Enabled' : 'Disabled'}</div>
          <div>Samples per Interrupt</div>
          <div>{samplesPerInterrupt.selectedOption}</div>
          <div>{stopInIdleMode.label}</div>
          <div>{stopInIdleMode.selectedOption}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Input Configuration'>
        <div className={styles['summary-options']}>
          <div>Input Scan</div>
          <div>{scanEnable.value ? 'Enabled' : 'Disabled'}</div>
          <div>{positiveInputA.label}</div>
          <div>{positiveInputA.visible ? `${positiveInputA.selectedOption}` : 'NA'}</div>
          <div>{positiveInputB.label}</div>
          <div>{positiveInputB.visible ? `${positiveInputB.selectedOption}` : 'NA'}</div>
          <div>{negativeInputA.label}</div>
          <div>{negativeInputA.visible ? `${negativeInputA.selectedOption}` : 'NA'}</div>
          <div>{negativeInputB.label}</div>
          <div>{negativeInputB.visible ? `${negativeInputB.selectedOption}` : 'NA'}</div>

          <div>{alternateInputSampleMode.label}</div>
          <div>{alternateInputSampleMode.selectedOption}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Output Configuration'>
        <div className={styles['summary-options']}>
          <div>{outputFormat.label}</div>
          <div>{outputFormat.selectedOption}</div>
          <div>{resultBufferMode.label}</div>
          <div>{resultBufferMode.selectedOption}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Sampling Configuration'>
        <div className={styles['summary-options']}>
          <div>{enableAutoSampling.label}</div>
          <div>{enableAutoSampling.value ? 'Enabled' : 'Disabled'}</div>
          <div>{stopAutoSamplingAfter1stConversionSequence.label}</div>
          <div>{stopAutoSamplingAfter1stConversionSequence.value ? 'Enabled' : 'Disabled'}</div>
          <div>{autoSampleTime.label}</div>
          <div>
            {conversionTriggerSource.selectedOption === 'Auto Convert'
              ? autoSampleTime.value
              : 'NA'}
          </div>
          <div>Conversion Trigger Source</div>
          <div>{conversionTriggerSource.selectedOption}</div>
        </div>
      </Fieldset>
    </div>
  );
}

const Summary = () => {
  return (
    <div>
      <Accordion
        activeIndex={0}
        style={{ minWidth: '50vw' }}>
        <AccordionTab header='ADC General Configuration'>
          <ADCConfigurationSummary />
        </AccordionTab>
        <AccordionTab header='Input Channel Scan Configuration'>
          <InputChannelScanConfiguration />
        </AccordionTab>
      </Accordion>
    </div>
  );
};

export default Summary;
