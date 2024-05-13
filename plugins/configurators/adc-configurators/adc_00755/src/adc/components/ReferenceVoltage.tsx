import { KeyValueSetSymbolHook } from '@mplab_harmony/harmony-plugin-client-lib';
import { RadioButton, RadioButtonProps } from 'primereact/radiobutton';
import { useEffect, useState } from 'react';

const ReferenceVoltage = (
  props: RadioButtonProps & { keyValueSetSymbolHook: KeyValueSetSymbolHook } & {
    classPrefix: string;
    classResolver?: (className: string) => string;
  }
) => {
  const { selectedOption, options, readOnly, visible, writeValue } = props.keyValueSetSymbolHook;
  const { keyValueSetSymbolHook, classPrefix, classResolver, ...onlyRadioButtonProps } = props;

  const [avdd, setAvdd] = useState<boolean>(false);
  const [vrefPlus, setVrefPlus] = useState<boolean>(false);
  const [avss, setAvss] = useState<boolean>(false);
  const [vrefMinus, setVrefMinus] = useState<boolean>(false);

  useEffect(() => {
    if (avdd && avss) {
      writeValue(options[0]);
    } else if (vrefPlus && vrefMinus) {
      writeValue(options[1]);
    } else if (avdd && vrefMinus) {
      writeValue(options[2]);
    } else if (vrefPlus && avss) {
      writeValue(options[3]);
    }
  }, [avdd, avss, vrefMinus, vrefPlus]);

  useEffect(() => {
    setAvdd(selectedOption.includes('AVDD'));
    setVrefPlus(selectedOption.includes('VREF+'));
    setAvss(selectedOption.includes('AVSS'));
    setVrefMinus(selectedOption.includes('VREF-'));
  }, [selectedOption]);

  const onClicking = (value: string) => {
    switch (value) {
      case 'AVDD':
        setAvdd(true);
        setVrefPlus(false);
        break;
      case 'VREF+':
        setAvdd(false);
        setVrefPlus(true);
        break;
      case 'AVSS':
        setAvss(true);
        setVrefMinus(false);
        break;
      case 'VREF-':
        setAvss(false);
        setVrefMinus(true);
        break;
    }
  };

  return !(props.hidden ?? !visible) ? (
    <>
      <RadioButton
        inputId={options[0]}
        disabled={readOnly}
        value={'AVDD'}
        tooltip={'AVDD'}
        onChange={(e) => onClicking('AVDD')}
        checked={avdd}
        {...onlyRadioButtonProps}
        className={classResolver ? classResolver(`${classPrefix}0`) : `${classPrefix}0`}
      />
      <RadioButton
        inputId={options[1]}
        disabled={readOnly}
        value='VREF+'
        tooltip='VREF+'
        onChange={(e) => onClicking('VREF+')}
        checked={vrefPlus}
        {...onlyRadioButtonProps}
        className={classResolver ? classResolver(`${classPrefix}1`) : `${classPrefix}1`}
      />
      <RadioButton
        inputId={options[2]}
        disabled={readOnly}
        value='AVSS'
        tooltip='AVSS'
        onChange={(e) => onClicking('AVSS')}
        checked={avss}
        {...onlyRadioButtonProps}
        className={classResolver ? classResolver(`${classPrefix}2`) : `${classPrefix}2`}
      />
      <RadioButton
        inputId={options[3]}
        disabled={readOnly}
        value='VREF-'
        tooltip='VREF-'
        onChange={(e) => onClicking('VREF-')}
        checked={vrefMinus}
        {...onlyRadioButtonProps}
        className={classResolver ? classResolver(`${classPrefix}3`) : `${classPrefix}3`}
      />
    </>
  ) : (
    <></>
  );
};

export default ReferenceVoltage;
