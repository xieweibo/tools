import os
import shutil
from subprocess import call, check_output


data = ['dlc2_215_05_movingon_01_02',
        'dlc2_215_05_movingon_01_03',
        'dlc2_215_05_movingon_01_04',
        'dlc2_215_05_movingon_01_05',
        'dlc2_215_05_movingon_01_06',
        'dlc2_215_05_movingon_01_07',
        'dlc2_215_05_movingon_01_08',
        'dlc2_215_05_movingon_01_09',
        'dlc2_215_05_movingon_01_10',
        'dlc2_215_05_movingon_01_11',
        'dlc2_215_05_movingon_01_13',
        'dlc2_215_05_movingon_01_15',
        'dlc2_215_05_movingon_01_16',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_02',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_03',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_04_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_04_02',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_04_03',
        'dlc2_220_sam_captain_fuelrods_briefing_00_00_04_04',
        'dlc2_220_sam_captain_fuelrods_briefing_00_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_03',
        'dlc2_220_sam_captain_fuelrods_briefing_00_05',
        'dlc2_220_sam_captain_fuelrods_briefing_00_05_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_samquestion_elaborate_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_samquestion_elaborate_02',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_samquestion_elaborate_03',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_samquestion_elaborate_04',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_samquestion_elaborate_06',
        'dlc2_220_sam_captain_fuelrods_briefing_00_06_nosamquestion',
        'dlc2_220_sam_captain_fuelrods_briefing_00_07',
        'dlc2_220_sam_captain_fuelrods_briefing_00_09',
        'dlc2_220_sam_captain_fuelrods_briefing_00_10',
        'dlc2_220_sam_captain_fuelrods_briefing_00_11',
        'dlc2_220_sam_captain_fuelrods_briefing_00_12',
        'dlc2_220_sam_captain_fuelrods_briefing_00_14',
        'dlc2_220_sam_captain_fuelrods_briefing_00_15',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_02',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_09',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_10_samfoundproof_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_10_samfoundproof_03',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_11_01',
        'dlc2_220_sam_captain_fuelrods_briefing_00_16_12',
        'dlc2_220_sam_captain_fuelrods_briefing_01_01',
        'dlc2_220_sam_captain_fuelrods_briefing_01_03',
        'dlc2_220_sam_captain_fuelrods_briefing_01_16',
        'dlc2_220_sam_captain_fuelrods_briefing_01_16_00',
        'dlc2_220_sam_captain_fuelrods_briefing_01_16_01',
        'dlc2_220_05_sam_captain_dislocationfix_01_03',
        'dlc2_220_05_sam_captain_dislocationfix_01_03_01',
        'dlc2_220_05_sam_captain_dislocationfix_01_03_03_meat',
        'dlc2_220_05_sam_captain_dislocationfix_01_03_03_nomeat',
        'dlc2_220_05_sam_captain_dislocationfix_01_05',
        'dlc2_220_05_sam_captain_dislocationfix_01_06',
        'dlc2_220_05_sam_captain_dislocationfix_01_09',
        'dlc2_220_05_sam_captain_dislocationfix_01_10',
        'dlc2_220_05_sam_captain_dislocationfix_01_11',
        'dlc2_220_05_sam_captain_dislocationfix_01_14',
        'dlc2_220_05_sam_captain_dislocationfix_01_15',
        'dlc2_220_05_sam_captain_dislocationfix_01_16',
        'dlc2_220_05_sam_captain_dislocationfix_01_17',
        'dlc2_220_05_sam_captain_dislocationfix_01_19',
        'dlc2_220_05_sam_captain_dislocationfix_01_21',
        'dlc2_220_05_sam_captain_dislocationfix_01_22',
        'dlc2_220_05_sam_captain_dislocationfix_01_23',
        'dlc2_220_05_sam_captain_dislocationfix_01_26',
        'dlc2_220_05_sam_captain_dislocationfix_01_27',
        'dlc2_220_05_sam_captain_dislocationfix_01_28',
        'dlc2_220_05_sam_captain_dislocationfix_01_29',
        'dlc2_220_05_sam_captain_dislocationfix_01_30',
        'dlc2_220_05_sam_captain_dislocationfix_01_31_01',
        'dlc2_220_07_sam_captain_partyallnight_01_01',
        'dlc2_220_07_sam_captain_partyallnight_01_02',
        'dlc2_220_07_sam_captain_partyallnight_01_03',
        'dlc2_220_07_sam_captain_partyallnight_01_04',
        'dlc2_220_07_sam_captain_partyallnight_01_05',
        'dlc2_220_07_sam_captain_partyallnight_01_06',
        'dlc2_220_07_sam_captain_partyallnight_01_08',
        'dlc2_220_07_sam_captain_partyallnight_01_09',
        'dlc2_220_07_sam_captain_partyallnight_01_11',
        'dlc2_220_07_sam_captain_partyallnight_drinking_01_01',
        'dlc2_220_07_sam_captain_partyallnight_drinking_01_02',
        'dlc2_220_07_sam_captain_partyallnight_drinking_01_03',
        'dlc2_220_07_sam_captain_partyallnight_drinking_01_04',
        'dlc2_220_07_sam_captain_partyallnight_drinking_01_05',
        'dlc2_220_07_sam_captain_partyallnight_02_01',
        'dlc2_220_07_sam_captain_partyallnight_02_03',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_01',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_02',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_03_positive_09',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_03_negative_03',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_03_negative_06',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_03_negative_07',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_04',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_06',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_07',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_08',
        'dlc2_220_07_sam_captain_partyallnight_03_samstory_09',
        'dlc2_220_07_sam_captain_partyallnight_04_01',
        'dlc2_220_07_sam_captain_partyallnight_04_02',
        'dlc2_220_07_sam_captain_partyallnight_04_03',
        'dlc2_220_07_sam_captain_partyallnight_05_01',
        'dlc2_220_07_sam_captain_partyallnight_05_02',
        'dlc2_220_07_sam_captain_partyallnight_05_03',
        'dlc2_220_07_sam_captain_partyallnight_05_04',
        'dlc2_220_07_sam_captain_partyallnight_05_06',
        'dlc2_220_07_sam_captain_partyallnight_05_07',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_03',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_05',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_08',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_09',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_10',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_11',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_14_01',
        'dlc2_220_sam_captain_fuelrods_briefing_01_04',
        'dlc2_220_sam_captain_fuelrods_briefing_01_05',
        'dlc2_220_sam_captain_fuelrods_briefing_01_09',
        'dlc2_220_sam_captain_fuelrods_briefing_01_14',
        'dlc2_220_sam_captain_fuelrods_briefing_01_14_01',
        'dlc2_220_sam_captain_fuelrods_briefing_01_14_02',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_16',
        'dlc2_220_07_sam_captain_partyallnight_partyend_01_17',
        'dlc2_220_10_sam_captain_firetraps_01_01',
        'dlc2_220_10_sam_captain_firetraps_01_03',
        'dlc2_270_90_sam_captain_beforebunker_00_01',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_02',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_03',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_04',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_05',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_06',
        'dlc2_270_90_sam_captain_beforebunker_00_putonsuit_01_07',
        'dlc2_270_90_sam_captain_beforebunker_00_02',
        'dlc2_270_90_sam_captain_beforebunker_00_03',
        'dlc2_270_90_sam_captain_beforebunker_00_04',
        'dlc2_270_90_sam_captain_beforebunker_00_07',
        'dlc2_280_sam_captain_beforebunker_01_01',
        'dlc2_280_sam_captain_beforebunker_01_03',
        'dlc2_280_sam_captain_beforebunker_01_04',
        'dlc2_280_sam_captain_beforebunker_01_05',
        'dlc2_280_sam_captain_beforebunker_01_06',
        'dlc2_280_sam_captain_beforebunker_01_07',
        'dlc2_280_sam_captain_beforebunker_01_09',
        'dlc2_280_sam_captain_beforebunker_01_15',
        'dlc2_280_sam_captain_beforebunker_01_16',
        'dlc2_280_sam_captain_beforebunker_01_16_01',
        'dlc2_280_sam_captain_beforebunker_01_18_01',
        'dlc2_280_sam_captain_beforebunker_01_18_03',
        'dlc2_280_sam_captain_beforebunker_01_19',
        'dlc2_280_sam_captain_beforebunker_01_20_00',
        'dlc2_300_sam_captain_afterbunker_01_01',
        'dlc2_300_sam_captain_afterbunker_01_01_01',
        'dlc2_300_sam_captain_afterbunker_01_01_03',
        'dlc2_300_sam_captain_afterbunker_01_01_04',
        'dlc2_300_sam_captain_afterbunker_01_02',
        'dlc2_300_sam_captain_afterbunker_01_03_01',
        'dlc2_300_sam_captain_afterbunker_01_03_06',
        'dlc2_300_sam_captain_afterbunker_01_03_10',
        'dlc2_350_sam_captain_samstory_start',
        'dlc2_350_sam_captain_samstory_short_02',
        'dlc2_350_sam_captain_samstory_long_06',
        'dlc2_350_sam_captain_samstory_long_08',
        'dlc2_400_sam_captain_returntothedock_01_01',
        'dlc2_400_sam_captain_returntothedock_01_02',
        'dlc2_400_sam_captain_returntothedock_01_03',
        'dlc2_400_sam_captain_returntothedock_01_04',
        'dlc2_400_sam_captain_returntothedock_01_05',
        'dlc2_300_sam_captain_afterbunker_01_04',
        'dlc2_300_sam_captain_afterbunker_01_05',
        'dlc2_300_sam_captain_afterbunker_01_06',
        'dlc2_300_sam_captain_afterbunker_01_07',
        'dlc2_300_sam_captain_afterbunker_01_08',
        'dlc2_300_sam_captain_afterbunker_01_09',
        'dlc2_300_sam_captain_afterbunker_01_10',
        'dlc2_300_sam_captain_afterbunker_01_11',
        'dlc2_300_sam_captain_afterbunker_01_12',
        'dlc2_300_sam_captain_afterbunker_01_13',
        'dlc2_300_sam_captain_afterbunker_01_14',
        'dlc2_300_sam_captain_afterbunker_01_15',
        'dlc2_300_sam_captain_afterbunker_01_16',
        'dlc2_300_sam_captain_afterbunker_01_17',
        'dlc2_300_sam_captain_afterbunker_01_18',
        'dlc2_400_sam_captain_returntothedock_05_06',
        'dlc2_400_sam_captain_returntothedock_05_07',
        'dlc2_400_sam_captain_returntothedock_05_08',
        'dlc2_400_10_sam_captain_returntothedock_06_01',
        'dlc2_400_10_sam_captain_returntothedock_06_02',
        'dlc2_400_10_sam_captain_returntothedock_06_03',
        'dlc2_400_10_sam_captain_returntothedock_06_04',
        'dlc2_400_10_sam_captain_returntothedock_06_05',
        'dlc2_400_10_sam_captain_returntothedock_06_06',
        'dlc2_400_10_sam_captain_returntothedock_06_07',
        'dlc2_400_10_sam_captain_returntothedock_06_08',
        'dlc2_400_10_sam_captain_returntothedock_06_09',
        'dlc2_400_10_sam_captain_returntothedock_06_10',
        'dlc2_400_10_sam_captain_returntothedock_06_11',
        'dlc2_400_10_sam_captain_returntothedock_06_12',
        'dlc2_400_10_sam_captain_returntothedock_06_13',
        'dlc2_400_10_sam_captain_returntothedock_06_14',
        'dlc2_400_10_sam_captain_returntothedock_06_15',
        'dlc2_400_10_sam_captain_returntothedock_06_16',
        'dlc2_400_10_sam_captain_returntothedock_06_16_01',
        'dlc2_400_20_sam_captain_returntothedock_07_01',
        'dlc2_400_20_sam_captain_returntothedock_07_02',
        'dlc2_400_20_sam_captain_returntothedock_07_03',
        'dlc2_400_20_sam_captain_returntothedock_07_04',
        'dlc2_400_20_sam_captain_returntothedock_07_05',
        'dlc2_400_20_sam_captain_returntothedock_07_06',
        'dlc2_400_20_sam_captain_returntothedock_07_07',
        'dlc2_400_20_sam_captain_returntothedock_07_08',
        'dlc2_400_30_sam_captain_returntothedock_08_01',
        'dlc2_400_30_sam_captain_returntothedock_08_02',
        'dlc2_500_treason_attackstarts_01_01',
        'dlc2_500_treason_attackstarts_01_02',
        'dlc2_500_treason_attackstarts_01_03',
        'dlc2_500_treason_attackstarts_01_04',
        'dlc2_500_treason_attackstarts_01_05',
        'dlc2_500_treason_attackstarts_01_06',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_02',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_05',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_08_01',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_09',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_10',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_11',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_12',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_13',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_14',
        'dlc2_500_10_treason_samklim_radio_confrontation_01_15',
        'dlc2_500_20_treason_samhasaplan_01_01',
        'dlc2_500_20_treason_samhasaplan_01_05',
        'dlc2_500_20_treason_samhasaplan_01_07',
        'dlc2_500_20_treason_samhasaplan_01_08',
        'dlc2_500_20_treason_samhasaplan_01_09',
        'dlc2_500_20_treason_samhasaplan_01_10',
        'dlc2_500_20_treason_samhasaplan_01_10_01',
        'dlc2_500_20_treason_samhasaplan_01_10_02',
        'dlc2_500_20_treason_samhasaplan_01_10_03',
        'dlc2_500_20_treason_samhasaplan_01_13',
        'dlc2_760_stairss_shootout_01_07',
        'dlc2_760_stairss_shootout_01_08',
        'dlc2_760_stairss_shootout_01_09',
        'dlc2_800_10_final_fight_01_03',
        'dlc2_800_10_final_fight_01_04',
        'dlc2_800_10_final_fight_01_05',
        'dlc2_800_10_final_fight_01_05_01',
        'dlc2_800_10_final_fight_01_11',
        'dlc2_800_20_final_fight_02_00',
        'dlc2_800_20_final_fight_02_01_klim_01',
        'dlc2_800_20_final_fight_02_01_klim_02',
        'dlc2_800_20_final_fight_02_01_klim_03',
        'dlc2_800_20_final_fight_02_02_klim_01',
        'dlc2_800_20_final_fight_02_02_klim_02',
        'dlc2_800_20_final_fight_02_02_klim_03',
        'dlc2_800_20_final_fight_02_03_klim_01',
        'dlc2_800_20_final_fight_02_03_klim_02',
        'dlc2_800_20_final_fight_02_03_klim_03',
        'dlc2_800_20_final_fight_02_04_klim_01',
        'dlc2_800_20_final_fight_02_04_klim_02',
        'dlc2_800_20_final_fight_02_04_klim_03',
        'dlc2_800_20_final_fight_02_05_klim_01',
        'dlc2_800_20_final_fight_02_05_klim_02',
        'dlc2_800_20_final_fight_02_05_klim_03',
        'dlc2_800_20_final_fight_02_06_klim_01',
        'dlc2_800_20_final_fight_02_06_klim_02',
        'dlc2_800_20_final_fight_02_06_klim_03',
        'dlc2_800_20_final_fight_02_07_klim_01',
        'dlc2_800_20_final_fight_02_07_klim_02',
        'dlc2_800_20_final_fight_02_07_klim_03',
        'dlc2_800_20_final_fight_02_08_klim_01',
        'dlc2_800_20_final_fight_02_08_klim_02',
        'dlc2_800_20_final_fight_02_08_klim_03',
        'dlc2_800_20_final_fight_02_09_klim_01',
        'dlc2_800_20_final_fight_02_09_klim_02',
        'dlc2_800_20_final_fight_02_09_klim_03',
        'dlc2_800_20_final_fight_02_10_klim_01',
        'dlc2_800_20_final_fight_02_10_klim_02',
        'dlc2_800_20_final_fight_02_10_klim_03',
        'dlc2_800_20_final_fight_02_10_klim_04',
        'dlc2_800_20_final_fight_02_10_klim_05',
        'dlc2_800_20_final_fight_02_10_klim_06',
        'dlc2_800_20_final_fight_02_10_klim_07',
        'dlc2_800_30_final_fight_03_01_01',
        'dlc2_800_30_final_fight_03_02_01',
        'dlc2_800_30_final_fight_03_02_02',
        'dlc2_800_30_final_fight_03_02_03',
        'dlc2_800_30_final_fight_03_02_04',
        'dlc2_800_30_final_fight_03_02_05',
        'dlc2_800_30_final_fight_03_02_07']

target_path = 'd:/.work/.tech/for_record_2/'
sounds = 'c:/SVN/content/sounds.us/voices/m3_dlc2/'
flac = '.flac'
wav = '.wav'
txt = '.txt'


def convert_to_wav(source, target):
    ffmpeg = 'c:/ffmpeg/bin/ffmpeg.exe'
    ffmpeg_command = (' ').join(
        [ffmpeg, '-i', source, target])
    call(ffmpeg_command, shell=True)


for path, dirs, names, in os.walk(sounds):

    for name in names:
        if flac not in name:
            continue
        bare_name = name.split(flac)[0]
        if bare_name in data:
            source_txt_path = os.path.join(path, bare_name + txt)
            target_txt_path = os.path.join(target_path, bare_name + txt)
            source_flac_path = os.path.join(path, bare_name + flac)
            target_wav_path = os.path.join(target_path, bare_name + wav)

            if os.path.exists(source_txt_path):
                shutil.copy2(source_txt_path, target_txt_path)
            else:
                print 'Not exists', source_txt_path

            convert_to_wav(source_flac_path, target_wav_path)
