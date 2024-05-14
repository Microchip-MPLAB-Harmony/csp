import { Accordion, AccordionTab } from 'primereact/accordion';
import { Fieldset } from 'primereact/fieldset';
import styles from './summary.module.css';
import { useContext } from 'react';
import { PluginConfigContext, useBooleanSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import useBlockDiagramViewModel from '../BlockDiagramViewModel';
import ChannelSequenceSummary from '../channel-sequence/ChannelSequenceSummary';

function ADCConfigurationSummary() {
  const {
    startEventInput,
    conversionTrigger,
    flushEventInput,
    enableRunInStandby,
    enableOnDemandControl,
    prescaler,
    resultResolution,
    positiveInputCombo,
    negativeInputCombo,
    accumulatedSampelsCombo,
    rightShiftsNumbers,
    sampleLength,
    referenceCombo,
    convTimeValue,
    highThresholdSpinner,
    lowThresholdSpinner,
    comparsionModeCombo,
    enableWinmonInterrupt,
    enableWinmonEvenOut,
    enableleft_alignedResult,
    enableResultInterrupt,
    enableResultIEvent
  } = useBlockDiagramViewModel();

  return (
    <div className={styles['summary-tab-container']}>
      <Fieldset legend='Input Configuration'>
        <div className={styles['summary-options']}>
          <div>Prescaler</div>
          <div>{prescaler.selectedOption}</div>
          <div>Sample Length (cycles)</div>
          <div>{sampleLength.value}</div>
          <div>Reference</div>
          <div>{referenceCombo.selectedOption}</div>
          <div>Conversion Time</div>
          <div>{convTimeValue}</div>
          <div>{accumulatedSampelsCombo.label}</div>
          <div>{accumulatedSampelsCombo.selectedOption}</div>
          <div>{rightShiftsNumbers.label}</div>
          <div>{rightShiftsNumbers.value}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Conversion Configuration'>
        <div className={styles['summary-options']}>
          <div>Conversion Trigger</div>
          <div>{conversionTrigger.value}</div>
          <div>{flushEventInput.label}</div>
          <div>{flushEventInput.selectedOption}</div>
          <div>{startEventInput.label}</div>
          <div>{startEventInput.selectedOption}</div>
        </div>
      </Fieldset>

      <Fieldset legend='Channel Configuration'>
        <div className={styles['summary-options']}>
          <div>Positive Input</div>
          <div>{positiveInputCombo.selectedOption}</div>
          <div>Negative Input</div>
          <div>{negativeInputCombo.selectedOption}</div>
        </div>
      </Fieldset>
      <Fieldset legend='Result Configuration'>
        <div className={styles['summary-options']}>
          <div>Result Resolution</div>
          <div>{resultResolution.selectedOption}</div>
          <div>{enableleft_alignedResult.label}</div>
          <div>{enableleft_alignedResult.value ? 'Enabled' : 'Disabled'}</div>
          <div>Result Ready Interrupt</div>
          <div>{enableResultInterrupt.value ? 'Enabled' : 'Disabled'}</div>
          <div>Result Ready Event Out</div>
          <div>{enableResultIEvent.value ? 'Enabled' : 'Disabled'}</div>
        </div>
      </Fieldset>
      <Fieldset legend='Window Mode Configuration'>
        <div className={styles['summary-options']}>
          <div>Window Monitor Mode</div>
          <div>{comparsionModeCombo.selectedOption}</div>
          <div>{highThresholdSpinner.label}</div>
          <div>{highThresholdSpinner.value}</div>
          <div>{lowThresholdSpinner.label}</div>
          <div>{lowThresholdSpinner.value}</div>
          <div>Window Monitor Interrupt</div>
          <div>{enableWinmonInterrupt.value ? 'Enabled' : 'Disabled'}</div>
          <div>Window Monitor Event Out</div>
          <div>{enableWinmonEvenOut.value ? 'Enabled' : 'Disabled'}</div>
        </div>
      </Fieldset>
      <Fieldset legend='Sleep Mode Configuration'>
        <div className={styles['summary-options']}>
          <div>{enableRunInStandby.label}</div>
          <div>{enableRunInStandby.value ? 'Enabled' : 'Disabled'}</div>
          <div>{enableOnDemandControl.label}</div>
          <div>{enableOnDemandControl.value ? 'Enabled' : 'Disabled'}</div>
        </div>
      </Fieldset>
    </div>
  );
}

const Summary = () => {
  const { componentId = 'adc' } = useContext(PluginConfigContext);
  const enableUserSequenceMode = useBooleanSymbol({ componentId, symbolId: 'ADC_SEQ_ENABLE' });
  return (
    <div>
      <Accordion
        activeIndex={0}
        style={{ minWidth: '50vw' }}>
        <AccordionTab header='ADC General Configuration'>
          <ADCConfigurationSummary />
        </AccordionTab>
        <AccordionTab header='Automatic Channel Sequences'>
          {enableUserSequenceMode.value ? (
            <ChannelSequenceSummary />
          ) : (
            <label>User Sequence Mode is disabled.</label>
          )}
        </AccordionTab>
      </Accordion>
    </div>
  );
};

export default Summary;
