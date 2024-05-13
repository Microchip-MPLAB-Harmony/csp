import { Accordion, AccordionTab } from 'primereact/accordion';
import { Fieldset } from 'primereact/fieldset';
import styles from './summary.module.css';
import useBlockDiagramViewModel from '../BlockDiagramViewModel';
import ChannelConfigurationSummary from '../channel-configuration/ChannelConfigurationSummary';
import ChannelSequenceSummary from '../channel-sequence/ChannelSequenceSummary';

function ADCConfigurationSummary() {
  const {
    conversionMode,
    triggerSelection,
    clockSource,
    clockFreq,
    prescalar,
    convTimeValue,
    resultResolution
  } = useBlockDiagramViewModel();

  return (
    <div className={styles['summary-tab-container']}>
      <Fieldset>
        <div className={styles['summary-options']}>
          <div>{conversionMode.label}</div>
          <div>{conversionMode.selectedOption}</div>
          <div>External Trigger Selection</div>
          <div>{triggerSelection.visible ? triggerSelection.selectedOption : 'NA'}</div>
          <div>Clock Source</div>
          <div>{clockSource.selectedOption}</div>
          <div>Prescalar</div>
          <div>{prescalar.value}</div>
          <div>{clockFreq.label}</div>
          <div>{clockFreq.value.toLocaleString()} Hz</div>
          <div>Conversion Time</div>
          <div>{convTimeValue}</div>
          <div>{resultResolution.label}</div>
          <div>{resultResolution.selectedOption}</div>
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
        <AccordionTab header='Channel Configuration'>
          <ChannelConfigurationSummary />
        </AccordionTab>
        <AccordionTab header='Channel Sequences'>
          <ChannelSequenceSummary />
        </AccordionTab>
      </Accordion>
    </div>
  );
};

export default Summary;
