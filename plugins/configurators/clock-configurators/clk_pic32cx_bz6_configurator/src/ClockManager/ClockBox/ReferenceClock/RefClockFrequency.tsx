import { useStringSymbol } from '@mplab_harmony/harmony-plugin-client-lib';
import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';

const RefClockFrequency = (props: {
  componentId: string;
  cx: (...classNames: string[]) => string;
}) => {
  const pbclk1Freq = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'CONFIG_SYS_CLK_PBCLK1_FREQ'
  });
  return (
    <div>
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(80000000)}
        className={props.cx('lbl_frcFreq1')}
      />
      <PlainLabel
        disPlayText={GetClockDisplayFreqValue(Number(pbclk1Freq.value))}
        className={props.cx('pbclk1Freq')}
        toolTip='Peripheral Clock 1-5, and 8 must not be more than 100 MHz.'
      />
    </div>
  );
};
export default RefClockFrequency;
