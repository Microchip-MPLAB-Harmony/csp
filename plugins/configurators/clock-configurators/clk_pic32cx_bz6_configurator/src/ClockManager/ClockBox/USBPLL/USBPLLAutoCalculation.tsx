import PlainLabel from 'clock-common/lib/Components/LabelComponent/PlainLabel';
import { Button } from 'primereact/button';
import { InputNumber } from 'primereact/inputnumber';
import { useEffect, useState } from 'react';
import { GetClockDisplayFreqValue } from 'clock-common/lib/Tools/Tools';
import {
  configSymbolApi,
  useCommentSymbol,
  useStringSymbol
} from '@mplab_harmony/harmony-plugin-client-lib';

const USBPLLAutoCalculation = (props: {
  componentId: string;
  usbPLLClk: number;
  usbclkPllInputFreq: number;
  close: (acceptStatus: boolean) => void;
}) => {
  const [usbPLLStateChange, setUsbPLLStateChange] = useState(false);
  const [buttonDisable, setButtonDisable] = useState(true);
  const [usbClockDisplayValue, setUsbClockDisplayValue] = useState(props.usbPLLClk);
  const symbol_USBPLL_freq = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'USBCLK'
  });
  const symbol_USBPLL_error = useStringSymbol({
    componentId: props.componentId,
    symbolId: 'UPLL_ERROR_PERC'
  });

  const upllOutofRange = useCommentSymbol({
    componentId: props.componentId,
    symbolId: 'UPLL_AUTO_CALC_ERROR_MSG'
  });
  useEffect(() => {
    setButtonDisable(upllOutofRange.visible);
  }, [upllOutofRange]);

  const singleDecimalFormat = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 5
  });

  const accept = () => {
    props.close(true);
  };
  const cancel = () => {
    props.close(false);
  };
  const usbPLLChanged = (newValue: number) => {
    RecalculateFreqencies1(newValue);
    setUsbClockDisplayValue(newValue);
    setButtonDisable(false);
    setUsbPLLStateChange(true);
  };

  const RecalculateFreqencies1 = (newValue: number) => {
    configSymbolApi.setValue(props.componentId, 'UPLL_REQUESTED_FOUT', newValue);
  };

  return (
    <div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Desired Frequency for UPLL : '} />
        </div>
        <div className='col-6'>
          <div className='flex flex-column'>
            <div className='flex flex-row'>
              <InputNumber
                value={usbClockDisplayValue}
                showButtons
                onValueChange={(target) => usbPLLChanged(Number(target.value))}
              />
              <PlainLabel
                disPlayText={' Hz'}
                className={'m-2'}
              />
            </div>
            {upllOutofRange.visible && usbPLLStateChange && (
              <PlainLabel
                disPlayText={upllOutofRange.label}
                redColorStatus={true}
              />
            )}
          </div>
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'PLL Input Frequency :'} />
        </div>
        <div className='col-6'>
          <PlainLabel disPlayText={GetClockDisplayFreqValue(props.usbclkPllInputFreq)} />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6 text-right'>
          <PlainLabel disPlayText={'Best Achievable Frequency :'} />
        </div>
        <div className='col-6  '>
          <PlainLabel
            disPlayText={GetClockDisplayFreqValue(Math.floor(Number(symbol_USBPLL_freq.value)))}
          />
        </div>
      </div>
      <div className='grid'>
        <div className='col-6  text-right'>
          <PlainLabel disPlayText={'% Error :'} />
        </div>
        <div className='col-6  '>
          <PlainLabel
            disPlayText={singleDecimalFormat.format(Number(symbol_USBPLL_error.value)) + ' %'}
          />
        </div>
      </div>

      <div className='flex flex-row-reverse'>
        <div className='flex align-items-center justify-content-center m-2'>
          <Button
            label={'Cancel'}
            onClick={cancel}
          />
        </div>
        <div className='flex align-items-center justify-content-center m-2'>
          <Button
            label={'Accept'}
            onClick={accept}
            disabled={buttonDisable}
          />
        </div>
      </div>
    </div>
  );
};
export default USBPLLAutoCalculation;
