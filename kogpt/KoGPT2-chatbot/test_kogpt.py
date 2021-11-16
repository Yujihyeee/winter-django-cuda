# https://jdh5202.tistory.com/850
# https://github.com/haven-jeon/KoGPT2-chatbot
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
import torch


class KoGpt2Class:
    def __init__(self):
        pass

    def execute(self):
        tokenizer = PreTrainedTokenizerFast.from_pretrained("skt/kogpt2-base-v2",
                                                            bos_token='</s>', eos_token='</s>', unk_token='<unk>',
                                                            pad_token='<pad>', mask_token='<mask>')

        model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
        text = '환경보전 어린이 폐차 '
        input_ids = tokenizer.encode(text)
        gen_ids = model.generate(torch.tensor([input_ids]),
                                 max_length=128,
                                 repetition_penalty=2.0,
                                 pad_token_id=tokenizer.pad_token_id,
                                 eos_token_id=tokenizer.eos_token_id,
                                 bos_token_id=tokenizer.bos_token_id,
                                 use_cache=True)
        generated = tokenizer.decode(gen_ids[0, :].tolist())
        print(generated)


class KoGpt3Class:
    def __init__(self):
        pass

    def execute(self):
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM

        tokenizer = AutoTokenizer.from_pretrained(
            'kakaobrain/kogpt', revision='KoGPT6B-ryan1.5b',
            bos_token='[BOS]', eos_token='[EOS]', unk_token='[UNK]', pad_token='[PAD]', mask_token='[MASK]'
        )
        model = AutoModelForCausalLM.from_pretrained(
            'kakaobrain/kogpt', revision='KoGPT6B-ryan1.5b',
            pad_token_id=tokenizer.eos_token_id,
            torch_dtype=torch.float16, low_cpu_mem_usage=True
        ).to(device='cuda', non_blocking=True)
        _ = model.eval()

        prompt = '인간처럼 생각하고, 행동하는 \'지능\'을 통해 인류가 이제까지 풀지 못했던'
        with torch.no_grad():
            tokens = tokenizer.encode(prompt, return_tensors='pt').to(device='cuda', non_blocking=True)
            gen_tokens = model.generate(tokens, do_sample=True, temperature=0.8, max_length=64)
            generated = tokenizer.batch_decode(gen_tokens)[0]

        print(generated)
        # print: 인간처럼 생각하고, 행동하는 '지능'을 통해 인류가 이제까지 풀지 못했던 문제의 해답을 찾을 수 있을 것이다.
        # 과학기술이 고도로 발달한 21세기를 살아갈 우리 아이들에게 가장 필요한 것은 사고력 훈련이다. 사고력 훈련을 통해, 세상


if __name__ == "__main__":
    k = KoGpt3Class()
    k.execute()
