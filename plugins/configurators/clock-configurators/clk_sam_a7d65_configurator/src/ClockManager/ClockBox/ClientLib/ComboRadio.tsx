import { ComboSymbolHook } from '@mplab_harmony/harmony-plugin-client-lib';
import { RadioButton, RadioButtonProps } from 'primereact/radiobutton';

const ComboRadio = (
  props: RadioButtonProps & { comboSymbolHook: ComboSymbolHook } & {
    classPrefix: string;
    classResolver?: (className: string) => string;
  }
) => {
  const { value, options, readOnly, visible, writeValue } = props.comboSymbolHook;
  const { comboSymbolHook, classPrefix, classResolver, ...onlyRadioButtonProps } = props;

  return !(props.hidden ?? !visible) ? (
    <>
      {options.map((option, i) => (
        <RadioButton
          key={option}
          inputId={option}
          name={classPrefix}
          disabled={readOnly}
          tooltip={options[i]}
          value={option}
          onChange={(e) => writeValue(option)}
          checked={option === value}
          {...onlyRadioButtonProps}
          className={classResolver ? classResolver(`${classPrefix}${i}`) : `${classPrefix}${i}`}
        />
      ))}
    </>
  ) : (
    <></>
  );
};

export default ComboRadio;
